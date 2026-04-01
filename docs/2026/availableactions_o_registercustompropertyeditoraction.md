# Операция: RegisterCustomPropertyEditorAction

**Параметр** |  **описание**
---|---
PropertyId |  Идентификатор свойства (= номер свойства)
PropertyIndex |  Индекс свойства
PropertyIdentName |  Идентифицирующее имя определенного пользователем свойства
Action |  Эта операция вызывается для обработки указанно свойства.
Editable |  1: Обработка поля возможна. 0: Обработка поля невозможна.
Register |  1: Регистрирует эту операцию. 0: Отменяет регистрацию этой операции.

С помощью операции вы можете изменять поведение свойств в таблице свойств. Если вы обрабатываете свойство в таблице свойств, вместо стандартного элемента управления отображается кнопка ++"..."++. Если нажать на кнопку ++"..."++, запустится указанная операция и вы сможете изменить отображаемое значение в отдельном диалоговом окне с указанным контекстом вызова.

Контекстом вызова зарегистрированной операции являются:

Параметр

PropertyId |  Идентификатор свойства
---|---
PropertyIndex |  Индекс свойства
PropertyIdentName |  Идентифицирующее имя определенного пользователем свойства
DbObjectId |  Ид. объекта, которому принадлежит свойство. В случае множественного выбора переносится только первый ид. объекта.
Value |  Отображаемая строка или многоязычная строка

Возвращенные значения

DialogModalResult |  1 для OK
---|---
DialogModified |  1 для модифицировано
Value |  Новое отображаемое значение или новая многоязычная строка

!!! example "Пример:"

    Регистрация диалогового окна для обработки свойства **Дополнительное поле** (ID 20901):RegisterCustomPropertyEditorAction
/Register:1
/Action:WPF_Demo_Custom_Editor
/PropertyId:20901
/PropertyIndex:1
/Editable:0Отмена регистрации диалогового окна для обработки свойства **Дополнительное поле** (ID 20901):RegisterCustomPropertyEditorAction
/Register:0
/Action:WPF_Demo_Custom_Editor
/PropertyId:20901
/PropertyIndex:1Регистрация диалогового окна для обработки определенного пользователем свойства:RegisterCustomPropertyEditorAction
/Register:1
/Action:WPF_Demo_Custom_Editor
/PropertyIdentName:Eplan.Page.UserSupplementaryField2
/Editable:1Отмена регистрации диалогового окна для обработки определенного пользователем свойства:RegisterCustomPropertyEditorAction
/Register:0
/Action:WPF_Demo_Custom_Editor
/PropertyIdentName:Eplan.Page.UserSupplementaryField2
