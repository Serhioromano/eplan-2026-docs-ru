# Операция: backup

**Параметр** |  **Описание**
---|---
TYPE |  Вид выполняемой задачи:
PROJECT: Резервирование всего проекта
MASTERDATA: Резервирование основных данных
PROJECTNAME |  Имя проекта с полным путем файла (является опцией).
Если не задано, то выбранный проект используется, когда операция вызывается через интерфейс пользователя (например, через сценарий или ленту). При вызове из командной строки Windows следует определить PROJECTNAME или сначала следует использовать `ProjectAction`. В противном случае отобразится системное сообщение.
ARCHIVENAME |  Имя архива.
Имя файла, в котором должны сохраняться данные резервирования (без указания пути).
DESTINATIONPATH |  Целевой каталог
COMMENT |  Комментарий для резервирования (необязательно).
Комментарий записывается в виде строки в соответствующем свойстве резервируемого проекта.
Значение по умолчанию: соответствующее свойство не задано.
AUTOCOPYREFDATA |  Указывает, следует ли перед резервированием копировать указанные данные (внешние документы, графические файлы) в соответствующий каталог проекта ( `...\ "Имя проекта"\DOC\\*.*` и `.\ "Имя проекта"\Images\\*.*`) (необязательно, 0 = нет, 1 = да).
Значение по умолчанию: 0
Действительно, только если параметр TYPE имеет следующее значение: PROJECT.
Изображения и документы, которые хранятся в проекте, всегда резервируются.
INCLEXTDOCS |  Указывает, следует ли учесть в резервировании внешние документы (необязательно, 0 = нет, 1 = да).
Значение по умолчанию: 0
INCLIMAGES  |  Указывает, следует ли учесть в резервировании графические файлы (необязательно, 0 = нет, 1 = да).
Значение по умолчанию: 0
BACKUPMETHOD |  Вид резервирования:
BACKUP: Проект резервируется
SOURCEOUT: Проект выгружается
ARCHIVE: Проект архивируется.
MDTYPE |  Тип резервируемых основных данных:
SYMBOLS: Библиотеки символов
MACROS: Макросы
FORMS: Формы
ARTICLES: Данные изделий
LANGUAGES: Словари
STANDARDSHEET: Рамки
STATIONDATA: Данные пользователя, рабочей станции
SOURCEPATH  |  Исходный каталог, применимо только при резервировании основных данных.
FILENAME |  Имя резервируемого файла.
Имя файла может быть введено с указанием или без указания полного пути.
Расширение имени файла должно быть указано.
Возможно расширение имени файла с заполнителями (пример: `/FILENAME:*.fn1`, `/FILENAME:*.*`, `/FILENAME:*sh)`.
Это относится только к резервированию основных данных.

!!! example "Пример:"

    Резервировать проект:backup
/TYPE:PROJECT
/DESTINATIONPATH:U:\temp
/ARCHIVENAME:EPLAN_Sample_Project.zw1
/COMMENT:Hello
/AUTOCOPYREFDATA:1
/INCLIMAGES:0
/INCLEXTDOCS:1backup
/TYPE:PROJECT
/PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk
/DESTINATIONPATH:U:\temp
/ARCHIVENAME:EPLAN_Sample_Project.zw1
/COMMENT:Hello
/BACKUPMETHOD:BACKUPРезервировать основные данные:Резервировать рамку с полным путем файла:backup
/TYPE:MASTERDATA
/FILENAME:C:\PlotFrames\EPLAN\ESS_A3DP.fn1
/SOURCEPATH:C:\PlotFrames\EPLAN
/DESTINATIONPATH:U:\temp
/ARCHIVENAME:my_MasterData
/COMMENT:"Hello world"
/MDTYPE:STANDARDSHEETРезервировать рамку без полного пути файла:backup
/TYPE:MASTERDATA
/FILENAME:ESS_A3DP.fn1
/SOURCEPATH:C:\PlotFrames\EPLAN
/DESTINATIONPATH:U:\temp
/ARCHIVENAME:my_MasterData
/COMMENT:"Hello world"
/MDTYPE:STANDARDSHEETРезервировать все рамки (*.fn1):backup
/TYPE:MASTERDATA
/FILENAME:*.fn1
/SOURCEPATH:C:\PlotFrames\EPLAN
/DESTINATIONPATH:U:\temp
/ARCHIVENAME:my_MasterData
/COMMENT:"Hello world"
/MDTYPE:STANDARDSHEETРезервировать все файлы (*.*) в указанном исходном каталоге:backup
/TYPE:MASTERDATA
/FILENAME:*.*
/SOURCEPATH:C:\PlotFrames\EPLAN
/DESTINATIONPATH:U:\temp
/ARCHIVENAME:my_MasterData
/COMMENT:"Hello world"
/MDTYPE:STANDARDSHEETРезервировать в указанном исходном каталоге все файлы (*.*), в расширении имени которых есть 'sh'.backup
/TYPE:MASTERDATA
/FILENAME:*sh
/SOURCEPATH:C:\PlotFrames\EPLAN
/DESTINATIONPATH:U:\temp
/ARCHIVENAME:my_MasterData
/COMMENT:"Hello world"
/MDTYPE:STANDARDSHEET

