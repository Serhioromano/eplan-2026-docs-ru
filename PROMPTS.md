This is MkDocs project. It is empty frame configured as I want it to look. I have to files 

1. file `tree.json` - contains structure tree
2. folder `docs/eplan` - contains files

Files are stored in Markdown format already. The name of the files matches end of the URL in structure tree ends with `.md` not `.htm` as in URL.

Can you modify `mkdocs.yml` and create a `nav:` structure according to structure tree.


At the end of each markdown file in `docs/new` there is a section

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

Other tasks for a file

1. Delete all double new lines and replace with a single empty line
2. In the lists starts with * or 1., 2., .. delete all white spaces because it starts like this

```md
  * Item1
  * Item2

  1. Item 3
  2. Item 4
```

3. At the beginning of each file delete any text before first title `## Это заголовок`
4. All links like `[ссылка](this_islink.htm)` change `.htm` to `.md`

Can you create a script that would make those changes to files and run it?
Do not delete that script it might be needed later.


Please analyze file `serve.log`. there you find something like this

```
WARNING -  Doc file 'eplan/wirenumberinggui_r_bezeichnung.md' contains a link 'wirenumberinggui_h_netzerweiterung.md', but the target 'eplan/wirenumberinggui_h_netzerweiterung.md' is not found among documentation files.
```

Please extract unfound file name and convert it to URL

https://www.eplan.help/ru-ru/Infoportal/Content/Plattform/2026/Content/htm/wirenumberinggui_h_netzerweiterung.htm

1. Change extension to `htm`
2. All URLs have to have same path

Create json file like `tree.json` with only one level of structure and put there all those links. keep json structure like in tree.json.