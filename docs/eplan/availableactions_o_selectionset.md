## Операция: selectionset

**Параметр** |  **Описание**  
---|---  
TYPE |  Вид выполняемой задачи:  
PROJECT: Возвращает текущий проект PROJECTS: Возвращает выбранные проекты  
PAGES: Возвращает выбранные страницы LAYOUTSPACES: Возвращает выбранные пространства листа  

!!! note "Замечание:"

    Результат выбора возвращается в вызываемом контексте:

!!! example "Пример:"

    Возвращает текущий выбранный проект:selectionset 
/TYPE:PROJECTРезультаты в вызываемом всплывающем меню: имя параметра = 'PROJECT'Значение = 'C:\Projects\EPLAN\EPLAN_Sample_Project.elk'Возвращает текущие выбранные проекты:selectionset 
/TYPE:PROJECTSРезультаты в вызываемом контексте: имя параметра = 'PROJECTS'Значение = 'C:\Projects\EPLAN\EPLAN_Sample_Project.elk;C:\Projects\EPLAN\EPLAN_Sample_Project2.elk'Возвращает текущие выбранные страницы:selectionset 
/TYPE:PAGESРезультаты в вызываемом всплывающем меню: имя параметра = 'PAGES'Значение = '=EB3+ET1/1;=EB3+ET1/2;=EB3+ET1/5'Возвращает текущие выбранные пространства листа:selectionset 
/TYPE:LAYOUTSPACESРезультаты в вызываемом контексте: имя параметра = 'LAYOUTSPACES'Значение = 'A1;A2;A3'

