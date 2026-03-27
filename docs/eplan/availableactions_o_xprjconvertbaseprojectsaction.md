# Операция: XPrjConvertBaseProjectsAction

**Параметр** |  **Описание**
---|---
ProjectTemplate |  Полный путь и имя шаблона проекта (*.ept или *.epb).
Folder |  Каталог, шаблоны проектов которого должны быть преобразованы в базовые проекты (*.zw9). Подкаталоги указанного каталога также учитываются.
FileTypes |  Тип файла для выполняемого преобразования: *.*: Преобразование всех шаблонов проектов *.ept: Преобразование всех шаблонов проектов ept *.epb: Преобразование всех шаблонов проектов epb

!!! example "Пример:"

    Преобразование отдельных шаблонов проектов:XPrjConvertBaseProjectsAction
/ProjectTemplate:$(MD_TEMPLATES)\IEC_tpl001.eptXPrjConvertBaseProjectsAction
/ProjectTemplate:$(MD_TEMPLATES)\GES_SBP.epbПреобразование всех шаблонов проектов в одном каталоге:XPrjConvertBaseProjectsAction
/Folder:$(MD_TEMPLATES)Преобразование конкретных типов файлов в одном каталоге:XPrjConvertBaseProjectsAction
/Folder:$(MD_TEMPLATES)
/FileTypes:*.ept

