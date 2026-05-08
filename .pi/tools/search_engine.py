#!/usr/bin/env python3
"""
Поисковый движок по документации EPLAN.
Гибрид: FTS5 (полнотекстовый) + TF-IDF (семантический).
Не требует внешних зависимостей кроме numpy и sqlite3 (stdlib).

Использование:
    python3 search_engine.py index          # построить индекс
    python3 search_engine.py "клеммная колодка"   # поиск
    python3 search_engine.py "макрос" --top 10    # топ-10 результатов
    python3 search_engine.py --stats               # статистика индекса
"""

import sqlite3
import json
import re
import os
import sys
import glob
import hashlib
from pathlib import Path
from typing import NamedTuple

import numpy as np

# === Конфигурация ============================================================
DOCS_DIR = Path(__file__).resolve().parent.parent.parent / "docs" / "2026"
DB_PATH = Path(__file__).resolve().parent.parent.parent / ".pi" / "cache" / "search_index.db"

# Русский стеммер (Портера) — базовый, но работает для технических терминов
VOWELS = "аеиоуыэюя"
PERFECTIVEGROUND = re.compile(r"((ив|ивши|ившись|ыв|ывши|ывшись)|((?<=[ая])(в|вши|вшись)))$")
REFLEXIVE = re.compile(r"(с[яь])$")
ADJECTIVE = re.compile(r"(ее|ие|ые|ое|ими|ыми|ей|ий|ый|ой|ем|им|ым|ом|его|ого|ему|ому|их|ых|ую|юю|ая|яя|ою|ею)$")
PARTICIPLE = re.compile(r"((ивш|ывш|ующ)|((?<=[ая])(ем|нн|вш|ющ|щ)))$")
VERB = re.compile(r"((ила|ыла|ена|ейте|уйте|ите|или|ыли|ей|уй|ил|ыл|им|ым|ен|ило|ыло|ено|ят|ует|уют|ит|ыт|ены|ить|ыть|ишь|ую|ю)|((?<=[ая])(ла|на|ете|йте|ли|й|л|ем|н|ло|но|ет|ют|ны|ть|ешь|нно)))$")
NOUN = re.compile(r"(а|ев|ов|ие|ье|е|иями|ями|ами|еи|ии|и|ией|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я)$")
SUPERLATIVE = re.compile(r"(ейш|ейше)$")
DERIVATIONAL = re.compile(r"(ост|ость)$")
I = re.compile(r"и$")
NN = re.compile(r"нн$")


def russian_stemmer(word: str) -> str:
    """Стеммер Портера для русского языка. Возвращает основу слова."""
    word = word.lower()
    if len(word) <= 2:
        return word
    # RV-область: после первой гласной
    m = re.search(rf"[{VOWELS}]", word)
    if not m:
        return word
    start = m.start() + 1
    pre, rv = word[:start], word[start:]
    if not rv:
        return pre
    # Шаг 1
    m = PERFECTIVEGROUND.search(rv)
    if m:
        rv = rv[: m.start()]
    else:
        rv = REFLEXIVE.sub("", rv, count=1)
        m = ADJECTIVE.search(rv)
        if m:
            rv = rv[: m.start()]
            rv = PARTICIPLE.sub("", rv, count=1)
        else:
            rv = VERB.sub("", rv, count=1)
            if not m:
                rv = NOUN.sub("", rv, count=1)
    # Шаг 2
    rv = I.sub("", rv, count=1)
    # Шаг 3
    rv = DERIVATIONAL.sub("", rv, count=1)
    # Шаг 4
    rv = SUPERLATIVE.sub("", rv, count=1)
    rv = NN.sub("н", rv, count=1)
    if not rv:
        rv = pre
    return pre + rv


class SearchResult(NamedTuple):
    path: str
    title: str
    score: float
    snippet: str


class SearchEngine:
    def __init__(self):
        self.db_path = DB_PATH
        self.docs_dir = DOCS_DIR
        self.stopwords = self._load_stopwords()

    def _load_stopwords(self) -> set:
        """Базовые русские стоп-слова."""
        return {
            "и", "в", "во", "не", "что", "он", "на", "я", "с", "со", "как", "а", "то",
            "все", "она", "так", "но", "его", "по", "из", "у", "же", "за", "бы",
            "от", "о", "для", "это", "или", "быть", "там", "при", "под", "мы",
            "до", "без", "через", "можно", "них", "был", "есть", "если", "когда",
            "того", "чем", "да", "об", "более", "ли", "также", "ведь", "нет",
            "очень", "тут", "себя", "раз", "была", "один", "после", "над", "около",
            "только", "два", "может", "них", "были", "которые", "the", "is", "of",
            "and", "to", "in", "this", "that", "for", "with", "are", "can",
            "к", "который", "весь", "где", "мой", "должен", "свой",
        }

    def _tokenize(self, text: str) -> list[str]:
        """Токенизация и стемминг текста."""
        words = re.findall(r"[а-яёa-z0-9]+", text.lower())
        return [russian_stemmer(w) for w in words if w not in self.stopwords and len(w) > 1]

    # ── Индексация ──────────────────────────────────────────────────────

    def index_all(self) -> int:
        """Полная индексация всех markdown-файлов в docs/2026/."""
        os.makedirs(self.db_path.parent, exist_ok=True)

        conn = sqlite3.connect(str(self.db_path))
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=OFF")

        # FTS5 таблица
        conn.execute("DROP TABLE IF EXISTS docs_fts")
        conn.execute("""
            CREATE VIRTUAL TABLE docs_fts USING fts5(
                path, title, content,
                tokenize='unicode61 remove_diacritics 1'
            )
        """)

        # TF-IDF таблица
        conn.execute("DROP TABLE IF EXISTS docs_meta")
        conn.execute("""
            CREATE TABLE docs_meta (
                path TEXT PRIMARY KEY,
                title TEXT,
                content TEXT,
                tokens TEXT,
                mod_time REAL
            )
        """)

        files = sorted(glob.glob(str(self.docs_dir / "*.md")))
        total = len(files)

        for i, filepath in enumerate(files):
            content = self._read_file(filepath)
            title = self._extract_title(content)
            tokens = self._tokenize(content)
            token_str = " ".join(tokens)

            conn.execute(
                "INSERT INTO docs_fts(path, title, content) VALUES(?, ?, ?)",
                (filepath, title, content),
            )
            conn.execute(
                "INSERT OR REPLACE INTO docs_meta(path, title, content, tokens, mod_time) "
                "VALUES(?, ?, ?, ?, ?)",
                (filepath, title, content, token_str, os.path.getmtime(filepath)),
            )

            if (i + 1) % 200 == 0:
                conn.commit()
                print(f"  Проиндексировано {i + 1}/{total} файлов...")

        conn.commit()
        conn.close()
        print(f"✓ Индексация завершена: {total} файлов")
        return total

    # ── Поиск ───────────────────────────────────────────────────────────

    def _raw_tokens(self, text: str) -> list[str]:
        """Токены без стемминга — для FTS5."""
        words = re.findall(r"[а-яёa-z0-9]+", text.lower())
        return [w for w in words if w not in self.stopwords and len(w) > 1]

    def search(self, query: str, top: int = 10) -> list[SearchResult]:
        """Гибридный поиск: FTS5 + TF-IDF переранжирование."""
        if not self.db_path.exists():
            print("Индекс не найден. Запустите: python3 search_engine.py index")
            return []

        conn = sqlite3.connect(str(self.db_path))

        # 1. FTS5 поиск (оригинальные токены, НЕ стеммированные)
        raw_tokens = self._raw_tokens(query)
        # Используем префиксный поиск: "клемм"* найдёт "клеммных", "клеммы" и т.д.
        fts_query = " OR ".join(f'"{t}"*' for t in raw_tokens)

        cursor = conn.execute(
            """
            SELECT path, title, content, rank
            FROM docs_fts
            WHERE docs_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (fts_query, max(top * 5, 50)),
        )
        candidates = list(cursor)

        if not candidates:
            conn.close()
            return []

        # 2. TF-IDF переранжирование (стеммированные токены для семантики)
        stemmed_tokens = self._tokenize(query)
        query_vec = self._tfidf_vector(stemmed_tokens)
        scored = []

        for path, title, content, fts_rank in candidates:
            doc_tokens = self._tokenize(content)
            doc_vec = self._tfidf_vector(doc_tokens)
            cosine = self._cosine_similarity(query_vec, doc_vec)

            # Комбинированный скор: FTS + TF-IDF
            fts_norm = max(0, 1.0 + float(fts_rank) / 100.0)
            combined = 0.4 * fts_norm + 0.6 * cosine

            snippet = self._make_snippet(content, raw_tokens)
            rel_path = os.path.relpath(path, self.db_path.parent.parent)

            scored.append(SearchResult(rel_path, title, combined, snippet))

        scored.sort(key=lambda x: x.score, reverse=True)
        conn.close()
        return scored[:top]

    # ── TF-IDF ──────────────────────────────────────────────────────────

    def _compute_idf(self) -> dict[str, float]:
        """Вычисление IDF по всему корпусу."""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.execute("SELECT tokens FROM docs_meta")
        doc_count = 0
        df = {}

        for (tokens_str,) in cursor:
            doc_count += 1
            unique = set(tokens_str.split())
            for token in unique:
                df[token] = df.get(token, 0) + 1

        conn.close()
        idf = {t: np.log((doc_count + 1) / (df[t] + 1)) + 1.0 for t in df}
        return idf

    def _tfidf_vector(self, tokens: list[str]) -> dict[str, float]:
        """TF-IDF вектор для набора токенов."""
        if not tokens:
            return {}
        total = len(tokens)
        tf = {}
        for t in tokens:
            tf[t] = tf.get(t, 0) + 1
        # Нормализованный TF
        tf = {t: c / total for t, c in tf.items()}
        return tf  # IDF применяется при cosine similarity

    def _cosine_similarity(self, vec1: dict, vec2: dict) -> float:
        """Косинусное сходство двух sparse-векторов."""
        if not vec1 or not vec2:
            return 0.0
        # Пересечение
        common = set(vec1.keys()) & set(vec2.keys())
        if not common:
            return 0.0

        dot = sum(vec1[k] * vec2[k] for k in common)
        norm1 = np.sqrt(sum(v * v for v in vec1.values()))
        norm2 = np.sqrt(sum(v * v for v in vec2.values()))

        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)

    # ── Вспомогательные ─────────────────────────────────────────────────

    def _read_file(self, path: str) -> str:
        with open(path, encoding="utf-8") as f:
            return f.read()

    def _extract_title(self, content: str) -> str:
        """Извлечение заголовка из markdown-файла."""
        for line in content.split("\n"):
            m = re.match(r"^#\s+(.+)", line)
            if m:
                return m.group(1).strip()
        return os.path.basename(content) if isinstance(content, str) else ""

    def _make_snippet(self, content: str, query_tokens: list[str], window: int = 80) -> str:
        """Формирование сниппета вокруг первого совпадения с запросом."""
        content_lower = content.lower()
        for token in query_tokens:
            idx = content_lower.find(token)
            if idx >= 0:
                start = max(0, idx - window)
                end = min(len(content), idx + window)
                snippet = content[start:end].replace("\n", " ")
                if start > 0:
                    snippet = "…" + snippet
                if end < len(content):
                    snippet += "…"
                return snippet
        # Fallback: первые 200 символов
        return content[:200].replace("\n", " ") + "…"

    # ── Статистика ─────────────────────────────────────────────────────

    def stats(self) -> dict:
        if not self.db_path.exists():
            return {"error": "Индекс не найден"}
        conn = sqlite3.connect(str(self.db_path))
        doc_count = conn.execute("SELECT COUNT(*) FROM docs_meta").fetchone()[0]
        # Средний размер документа
        avg_len = conn.execute(
            "SELECT AVG(LENGTH(content)) FROM docs_meta"
        ).fetchone()[0]
        conn.close()
        return {
            "documents": doc_count,
            "avg_chars_per_doc": round(avg_len or 0),
            "index_size_kb": round(os.path.getsize(self.db_path) / 1024, 1),
        }


# === CLI =====================================================================

def _parse_args(args: list[str]) -> tuple[str, int, bool]:
    """Разбор аргументов: (query, top, use_json)."""
    query_parts = []
    top = 10
    use_json = False
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--top" and i + 1 < len(args):
            top = int(args[i + 1])
            i += 2
        elif a == "--json":
            use_json = True
            i += 1
        else:
            query_parts.append(a)
            i += 1
    return " ".join(query_parts), top, use_json


def _output(results: list, use_json: bool):
    """Вывод результатов: текст или JSON."""
    if use_json:
        out = [
            {
                "rank": i + 1,
                "score": round(r.score, 3),
                "title": r.title,
                "path": r.path,
                "snippet": r.snippet,
            }
            for i, r in enumerate(results)
        ]
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        if not results:
            print("Ничего не найдено.")
        else:
            for i, r in enumerate(results):
                print(f"\n#{i + 1} [{r.score:.2f}] {r.title}")
                print(f"   Файл: {r.path}")
                print(f"   {r.snippet}")


if __name__ == "__main__":
    engine = SearchEngine()

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "index":
        print("Индексация документации EPLAN...")
        n = engine.index_all()
        s = engine.stats()
        print(f"  Файлов: {s['documents']}")
        print(f"  Размер индекса: {s['index_size_kb']} КБ")
        print(f"  Средний размер документа: {s['avg_chars_per_doc']} символов")

    elif cmd == "--stats":
        s = engine.stats()
        print(json.dumps(s, indent=2, ensure_ascii=False))

    elif cmd in ("search", "s"):
        query, top, use_json = _parse_args(sys.argv[2:])
        if not query:
            print("Укажите поисковый запрос")
            sys.exit(1)
        results = engine.search(query, top=top)
        _output(results, use_json)

    else:
        # Поиск по умолчанию (первый аргумент — запрос)
        query, top, use_json = _parse_args(sys.argv[1:])
        results = engine.search(query, top=top)
        _output(results, use_json)
