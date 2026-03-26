This is MkDocs project. It is empty frame configured as I want it to look. I have to files 

1. file `tree.json` - contains structure tree
2. folder `docs/eplan` - contains files

Files are stored in Markdown format already. The name of the files matches end of the URL in structure tree ends with `.md` not `.htm` as in URL.

Can you modify `mkdocs.yml` and create a `nav:` structure according to structure tree.

At the end of each markdown file in `docs/eplan` there is a section

Пример

```
См. также

[Преобразование вспомогательной функции в главную](eplan/adjustdata_h_nebenfunktionaendern.md)

[Преобразовать излишние главные функции](eplan/adjustdata_h_funktionkorrigieren.md)

[Синхронизировать распределенно представленные функции](eplan/adjustdata_h_funktionabgleichen.md)
```

Я хочу получить

```
**См. также:**

* [Преобразование вспомогательной функции в главную](eplan/adjustdata_h_nebenfunktionaendern.md)
* [Преобразовать излишние главные функции](eplan/adjustdata_h_funktionkorrigieren.md)
* [Синхронизировать распределенно представленные функции](eplan/adjustdata_h_funktionabgleichen.md)
```

1. Make `См. также` bold
2. Place `:` after `См. также`
3. Make links into markdown list
4. Delete lines between links
5. Have one line after `См. также`

can you create a script that would make those changes to files and run it?
