# Операция: XCabCalculateEnclosureTotalWeightAction

**Параметр** |  **Описание**
---|---
ProjectName |  Имя проекта с полным путем файла (является опцией).
Если заданный проект не открыт, он автоматически открывается при выполнении данной операции и снова закрывается после завершения операции. Без действительного указания используется открытый в настоящее время проект.
DatabaseId |  Идентификатор проекта для проекта (является опцией). При использовании данного параметра необходимо перед выполнением операции открыть проект в Eplan Electric P8. Без действительного указания используется открытый в настоящее время проект. Если указывается параметр `ProjectName`, параметр `DatabaseID` игнорируется.
CabinetTotalWeight |  Общий вес одного отдельного электрошкафа.

!!! example "Пример:"

    XCabCalculateEnclosureTotalWeightAction
/DatabaseId:28
XCabCalculateEnclosureTotalWeightAction
/ProjectName:C:\Projects\EPLAN\EPLAN_Sample_Project.elk
