# Операция: XSDPreviewAction

**Параметр** |  **описание**
---|---
PROJECTNAME  |  Имя проекта. При отсутствии пути используется значение по умолчанию (см. $(MD_PROJECTS)).
PAGENAME  |  Имя страницы в виде символьной строки
MACRONAME  |  Полный путь к макросу страницы или окна (с расширением). При отсутствии пути используется значение по умолчанию (см. $(MD_MACROS)).
SHOW  |  1: Открывается предварительный просмотр страницы/макроса; 0: Предварительный просмотр закрывается.

!!! example "Пример:"

    Предварительный просмотр страницы:XSDPreviewAction
    /PROJECTNAME:ESS_Sample_Project
    /PAGENAME:=CA1+EAA/1XSDPreviewAction
    /PROJECTNAME:"C:\...\EPLAN\Electric P8\Projects\...\ESS_Sample_Project"
    /PAGENAME:=CA1+EAA/2Предварительный просмотр макроса страницы:XSDPreviewAction
    /PROJECTNAME:ESS_Sample_Project
    /MACRONAME:Macro_0001.emaXSDPreviewAction
    /PROJECTNAME:$(MD_PROJECTS)\ESS_Sample_Project
    /MACRONAME:$(MD_MACROS)\Macro_0001.ema

С вашей помощью мы можем улучшить работу системы. Мы документируем ваши действия в Google Analytics, чтобы постоянно совершенствовать справочную систему ([Дополнительная информация и возможности подачи возражений](helpsystem_hinweise_optout.md)).

Скрыть сообщение
