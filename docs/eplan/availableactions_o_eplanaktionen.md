# Операции Eplan: Обзор

В Eplan вам доступны нижеперечисленные операции для различных областей применения. "X" в столбце обозначает область применения, рекомендуемую нами для соответствующей операции. Обозначенные "X*" в столбце Лента операции доступны в диалоговом окне Настроить для настройки ленты в качестве предварительно заданных команд.

В справке Eplan API по платформе приведена дополнительная информация об операциях. Список всех официальных операций Eplan приведен в разделе [Actions](https://www.eplan.help/en-US/Infoportal/content/api/2024/API Actions.html).

Имя операции |  Командная строка |  Сценарии |  Лента |  Описание
---|---|---|---|---
[backup](availableactions_o_backup.md) | X | X | – |  Резервирует проект или основные данные.
[changelayer](availableactions_o_changelayer.md) | X | X | – |  Изменяет графические свойства слоев.
[check](availableactions_o_check.md) | X | X | – |  Проверяет страницы или весь проект.
[CleanWorkspaceAction](availableactions_o_xsvcleanworkspaceaction.md) | X | – | – |  Удаляет существующую рабочую область.
[compress](availableactions_o_compress.md) | X | X | – |  Сжимает проект.
[devicelist](availableactions_o_devicelist.md) | X | X | – |  Импортирует, экспортирует или удаляет список устройств.
[edit](availableactions_o_edit.md) | X | X | – |  Открывает страницу или проект.
[EplApiModuleAction](availableactions_o_eplapimoduleaction.md) | X | – | – |  Загружает и регистрирует модуль API.
[EsCorrectConnections](availableactions_o_escorrectconnections.md) | X | – | X |  Объединяет идентичные точки определения соединения.
[ExecuteScript](availableactions_o_executescript.md) | X | – | X |  Выполняет сценарий.
[export](availableactions_o_export.md) | X | X | – |  Экспортирует страницы или проекты в различных форматах.
[export3D](availableactions_o_export3d.md) | X | X | – |  Экспортирует пространство листа в формат STEP.
[exportNCData](availableactions_o_exportncdata.md) | X | X | – |  Экспортирует данные ЧУ для различных форматов машин.
[exportProductionWiring](availableactions_o_exportProductionWiring.md) | X | X | – |  Экспортирует данные сборки проводов в различных форматах.
[ExportSegmentsTemplate](availableactions_o_exportsegmentstemplate.md) | X | X | – |  Экспортирует шаблоны сегментов в файл.
[exportToGraphics](availableactions_o_exporttographics.md) | X | X | – |  Экспортирует страницы или проекты в графическом формате (TIF, GIF, PNG, JPG).
gedRedraw | – | – | X |  Заново выстраивает рисунок графического редактора.
[generate](availableactions_o_generate.md) | X | X | – |  Генерирует соединения или кабели.
[generatemacros](availableactions_o_generatemacros.md) | X | X | – |  Генерирует макросы из проекта.
[GraphicalLayerTable](availableactions_o_GraphicalLayerTable.md) | X | X | – |  Импортирует / экспортирует слои.
[import](availableactions_o_import.md) | X | X | – |  Импортирует проекты, макросы или чертежи.
[import3d](availableactions_o_import3d.md) | X | X | – |  Импортирует трехмерные графические данные.
[ImportPrePlanningData](availableactions_o_importpreplanningdata.md) | X | X | – |  Импортирует данные предварительного планирования.
[ImportSegmentsTemplate](availableactions_o_importsegmentstemplate.md) | X | X | – |  Импортирует шаблоны сегментов из файла в проект.
[InsertModelViewAction](availableactions_o_InsertModelViewAction.md) | X | X | – |  Добавляет обзоры модели в проект.
[label](availableactions_o_label.md)
Лента Экспортировать данные изготовления / вывести маркировку | X | X | X* |  Генерирует экспорт данных изготовления / маркировку для проекта.
[masterdata](availableactions_o_masterdata.md) | X | X | – |  Обновляет основные данные текущего проекта.
[MfExportRibbonBarAction](availableactions_o_mfexportribbonbaraction.md) | X | X | – |  Экспортирует ленту.
[MfImportRibbonBarAction](availableactions_o_mfimportribbonbaraction.md) | X | X | – |  Импортирует ленту.
[OpenWorkspaceAction](availableactions_o_xsvopenworkspaceaction.md) | – | – | X |  Открывает существующую рабочую область.
[partslist](availableactions_o_partslist.md) | X | X | – |  Импортирует или экспортирует спецификацию.
[partsmanagementapi](availableactions_o_partsmanagementapi.md) | X | X | – |  Экспортирует или импортирует изделия и другие объекты управления изделиями, такие как списки принадлежностей, размещения принадлежностей, схемы сверления, схемы соединений и адреса.
[plcservice](availableactions_o_plcservice.md) | X | X | – |  Импортирует или экспортирует данные ПЛК посредством приведенной программы конфигурации.
[preparemacros](availableactions_o_preparemacros.md) | X | X | – |  Подготавливает макросы проекта макросов для автоматической генерации.
[print](availableactions_o_print.md) | X | X | – |  Печатает страницу или весь проект.
[ProjectAction](availableactions_o_xesprojectaction.md) | X | X | – |  Выполняет операцию для проекта, а затем закрывает проект.
[projectmanagement](availableactions_o_projectmanagement.md)
Лента: Управлять проектом | X | X | X* |  Выполняет операцию для управления проектами или для проектов. Одним из вариантов является реорганизация проекта. Это позволяет во многих случаях исправить проекты с ошибками базы данных, а затем снова открыть их.
[ProjectOpen](availableactions_o_projectopen.md) | X | X | – |  Открывает проект.
[RegisterCustomPropertyEditorAction](availableactions_o_registercustompropertyeditoraction.md) | – | X | – |  Регистрирует / отменяет регистрацию определенного пользователем диалогового окна для обработки номера свойства или идентифицирующего имени определенного пользователем свойства.
[RegisterScript](availableactions_o_registerscript.md) | X | – | – |  Регистрирует сценарий.
[Renumber](availableactions_o_renumber.md) | X | X | – |  Выполняет нумерацию.
[reports](availableactions_o_reports.md) | X | X | – |  Генерирует отчет по проекту.
[restore](availableactions_o_restore.md) | X | X | – |  Восстанавливает проект или основные данные.
[SaveWorkspaceAction](availableactions_o_xsvsaveworkspaceaction.md) | – | – | X |  Сохраняет текущие настройки интерфейса как рабочую область.
[search](availableactions_o_search.md) | X | X | X |  Осуществляет поиск объектов (устройств, свойств, текстов и т. д.) в проекте.
[selectionset](availableactions_o_selectionset.md) | – | X | – |  Извлекает значения (имя, путь файла, расширение имени файла) выбранных страниц или выбранного проекта.
[SetProjectLanguage](availableactions_o_xessetprojectlanguageaction.md) | X | X | – |  Настраивает языки отображения для обрабатываемых и защищенных от записи проектов.
[subprojects](availableactions_o_subprojects.md) | X | X | – |  Выгружает частичный проект и снова сохраняет его.
[SwitchProjectType](availableactions_o_switchprojecttype.md) | X | X | – |  Переключает свойство "Вид проекта".
[synchronize](availableactions_o_synchronize.md) | X | X | – |  Синхронизирует данные проекта.
[Topology](availableactions_o_Topology.md) | X | X | – |  Маршрутизирует соединения топологии или генерирует функции топологии.
[translate](availableactions_o_translate.md) | X | X | – |  Переводит проект, удаляет перевод из проекта или экспортирует список отсутствующих слов.
[UnregisterScript](availableactions_o_unregisterscript.md) | X | – | – |  Отменяет регистрацию сценария.
[UpdateSegmentsFilling](availableactions_o_UpdateSegmentsFilling.md) | X | X | – |  Рассчитывает для всего проекта значение свойства Топология: Степень заполнения (ид. 20332) ручных сегментов маршрутизации и вносит его в сегменты маршрутизации, т. е. сообщает о наличии свободного места в ручных сегментах маршрутизации.
[XAfActionSetting](availableactions_o_xafactionsetting.md)
Лента: Установить настройку | X | X | X* |  Устанавливает определенное значение для настроек пользователя, станции и фирмы.
[XAfActionSettingProject](availableactions_o_xafactionsettingproject.md)
Лента: Установить проектную настройку | X | X | X* |  Устанавливает определенное значение для настройки проекта.
[XAMlExportProductionData2RASCenterAction](availableactions_o_xamlexportproductiondata2rascenteraction.md) | X | X | X |  Экспортирует данные изготовления для выбранного проекта механической обработки электрошкафов в формате AutomationML. Сгенерированный файл AML предназначен для импорта в программу планирования и управления изготовлением Rittal - RiPanel Processing Center.
[XCabCalculateEnclosureTotalWeightAction](availableactions_o_xcabcalculateenclosuretotalweightaction.md) | X | X | X |  Рассчитывает общий вес для каждого электрошкафа выбранного проекта и записывает результат в свойство Общий вес (ид. 36108) соответствующего размещения изделия.
[XCCreateGravingtextAction](availableactions_o_xccreategravingtextaction.md)
Лента: Кабели: Генерировать текст гравировки | X | – | X* |  Генерировать текст гравировки из ОУ источника и цели кабеля. Обозначение сокращено в соответствии со стандартом VASS (Volkswagen Audi Seat Skoda).
[XCMRemoveUnnecessaryNDPsAction](availableactions_o_XCMRemoveUnnecessaryNDPsAction.md) | X | X | – |  Удаляет лишние точки определения сети из текущего проекта. При необходимости точки определения соединения размещаются на соединениях сети для предотвращения потери свойств.
[XCMUserToolAction](availableactions_o_XCMUserToolAction.md)
Лента: Выполнить внешнюю программу | – | – | X* |  Позволяет интегрировать внешние программы.
XCMUniteNetDefinitionPointsAction | X | X | – |  Объединяет точки определения сети, размещенные в одной и той же сети текущего проекта. При размещении нескольких точек определения сети в одной и той же сети эти точки (то есть их соединения) объединяются в одной точке определения сети. Таким образом, после выполнения данной операции каждая сеть имеет не больше одной точки определения сети, в которой содержатся все сетевые соединения сети.
[XDLInsertDeviceAction](availableactions_o_xdlinsertdeviceaction.md)
Лента: Вставить устройство | X | X | X* |  Вставляет устройство.
[XEGActionInsertSymRef](availableactions_o_xegactioninsertsymref.md)
Лента: Вставить символ, Вставить символ с определением функции | – | – | X* |  Добавляет символ.
[XEsGetPagePropertyAction](availableactions_o_xesgetpagepropertyaction.md) | – | X | – |  Определяет значение свойства страницы для выбранной в данный момент страницы.
[XEsGetProjectPropertyAction](availableactions_o_xesgetprojectpropertyaction.md) | – | X | – |  Определяет значение свойства проекта для выбранного в данный момент проекта.
[XEsGetPropertyAction](availableactions_o_xesgetpropertyaction.md) | – | X | – |  Определяет значение свойства выбранного в данный момент объекта в графическом редакторе.
[XEsSetPagePropertyAction](availableactions_o_xessetpagepropertyaction.md)
Лента: Установить свойство страницы | – | – | X* |  Устанавливает определенное значение свойства страницы для текущей выбранной страницы.
[XEsSetProjectPropertyAction](availableactions_o_xessetprojectpropertyaction.md)
Лента: Установить свойство проекта | – | – | X* |  Устанавливает определенное значение свойства проекта для текущего выбранного проекта.
[XEsSetPropertyAction](availableactions_o_xessetpropertyaction.md)
Лента: Установить свойство усл. обозначения | – | – | X* |  Устанавливает определенное значение свойства для свойства текущих выбранных объектов.
[XEsUserPropertiesExportAction](availableactions_o_xesuserpropertiesexportaction.md) | X | X | – |  Экспортирует определенные пользователем свойства в файл.
[XEsUserPropertiesImportAction](availableactions_o_xesuserpropertiesimportaction.md) | X | X | – |  Импортирует определенные пользователем свойства из файла.
XGedClosePage | – | – | X |  Закрывает все выбранные страницы. У данной операции нет параметров.
[XGedStartInteractionAction](availableactions_o_xgedstartinteractionaction.md)
Лента: Установить формат графич. элементов, Вставить макроc, Установить формат усл. обознач., Установ. формат текста, Установить формат графики соединений (точки определения соединения, точки определения потенциала) | – | X | X* |  Запускает диалог в графическом редакторе. К числу возможных взаимодействий относится, например, вставка макроса или задание настроек форматирования для условных обозначений, текстов или подобных элементов.
[XGedUpdateMacroAction](availableactions_o_xgedupdatemacroaction.md) | X | X | – |  Обновляет макрос.
[XMActionDCCommonExport ](availableactions_o_XMActionDCCommonExport.md) | X | X | – |  Запускает экспорт для внешней обработки.
[XMActionDCImport](availableactions_o_xmactiondcimport.md) | X | X | – |  Импортирует файл конфигурации данных внешней обработки в существующий проект Eplan.
[XMDeleteReprTypeAction](availableactions_o_xmdeletereprtypeaction.md) | X | X | – |  Удаляет из выбранного макроса вид представления и резервирует эти макросы в каталоге.
[XMExportConnectionsAction](availableactions_o_xmexportconnectionsaction.md)
Лента: Экспортировать соединения | X | X | X* |  Экспортирует свойства соединений проекта для внешней обработки.
[XMExportDCArticleDataAction](availableactions_o_xmexportdcarticledataaction.md) | X | X | – |  Запускает экспорт данных изделия для внешней обработки.
[XMExportFunctionAction](availableactions_o_xmexportfunctionaction.md)
Лента: Экспортировать функции | X | X | X* |  Экспортирует свойства функций проекта для внешней обработки.
[XMExportPagesAction](availableactions_o_xmexportpagesaction.md)
Лента: Экспортировать страницы | X | X | X* |  Экспортирует свойства страниц проекта для внешней обработки.
[XMImportDCArticleDataAction](availableactions_o_xmimportdcarticledataaction.md) | X | X | – |  Импортирует файл с данными изделия после внешней обработки в существующую базу данных изделий Eplan.
[XPamsDeviceSelectionAction](availableactions_o_xpamsdeviceselectionaction.md) | X | X | – |  Осуществляет выбор устройства или обновляет данные устройства.
[XPamSelectPart ](availableactions_o_XPamSelectPart.md) | X | X | – |  Запускает выбор изделия.
[XPartsSetDataSourceAction](availableactions_o_xpartssetdatasourceaction.md) | X | X | X |  Задает настройку для источника базы данных в управлении изделиями.
[XPlaUpdateDetailAction](availableactions_o_XPlaUpdateDetailAction.md) | X | X | – |  Обновляет детальное планирование в навигаторе предварительного планирования.
[XPrjActionUpgradeProjects](availableactions_o_XPrjActionUpgradeProjects.md) | X | X | – |  Обновляет один или несколько проектов до текущей схемы базы данных.
[XPrjConvertBaseProjectsAction](availableactions_o_xprjconvertbaseprojectsaction.md) | X | X | – |  Преобразует шаблоны проектов из старых версий Eplan (версия 2.9 и старше) в базовые проекты.
[XSDPreviewAction](availableactions_o_xsdpreviewaction.md) | X | X | – |  Открывает или закрывает предварительный просмотр страницы или макроса.
[XSettingsExport](availableactions_o_xsettingsexport.md) | X | X | – |  Экспортирует настройки пользователя, настройки станции и фирмы.
[XSettingsImport](availableactions_o_xsettingsimport.md)
Лента: Импортировать настройки | X | X | X* |  Импортирует настройки пользователя, настройки станции и фирмы.
[XSettingsRegisterAction](availableactions_o_XSettingsRegisterAction.md) | X | – | – |  Позволяет регистрировать Add-ons.
[XSettingsUnregisterAction](availableactions_o_XSettingsUnregisterAction.md) | X | – | – |  Позволяет отменить регистрацию Add-ons.

!!! warning "Предупреждение:"

    Обратите внимание, что примеры, приведенные в темах справки для отдельных операций, для удобочитаемости снабжены разрывами строк. Если вы хотите использовать примеры в представленной форме, необходимо обязательно удалить разрывы строк! Кроме того, следите за тем, чтобы операция и параметр, а также параметры между собой были разделены при вводе знаком пробела.

**См. также:**

* [Операции Eplan](availableactions_k_start.md)
