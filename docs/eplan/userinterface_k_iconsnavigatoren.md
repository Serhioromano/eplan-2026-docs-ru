# Пиктограммы в навигаторах

В следующей таблице перечислены самые важные пиктограммы, использующиеся в нескольких навигаторах данных проекта, и их значения.

Если в представлениях в виде дерева навигаторов данных проекта навести курсор на пиктограмму, можно будет увидеть краткий текст с информацией про эту пиктограмму (всплывающая подсказка). Если пиктограммы объединены (например, ![](images/navigatorgui_mainfunctionpart_as.png)![](images/navigatorgui_function_as.png) для размещенной многополюсной главной функции), то для каждой пиктограммы будет отображаться отдельная всплывающая подсказка.

Специфические пиктограммы расшифровываются в соответствующих диалоговых окнах навигатора.

Пиктограмма |  Значение
---|---
![](images/all_project_as.png) |  Обозначает уровень проекта. Эти пиктограммы отображаются только в том случае, если открыто несколько проектов.
![](images/projectstructure_functionalassignment_as.png), ![](images/projectstructure_higherlevelfunction_as.png), ![](images/projectstructure_installationsite_as.png), ![](images/projectstructure_mountinglocation_as.png), ![](images/projectstructure_installationnr_as.png), ![](images/projectstructure_userdefined_as.png) |  Уровень структуры проекта (вид предшествующего знака для функционального присвоения, функционального назначения, места сборки, места установки, номера установки, определенной пользователем структуры)
![](images/all_prefixicon_projectstructure.png) |  Предшествующая цифра
![](images/Identifier_as.png) |  Префикс/буквенное обозначение
![](images/all_countericon_projectstructure.png) |  Счетчик
![](images/navigatorgui_subcounter_as.png) |  Подсчетчик
![](images/navigatorgui_device_as.png) |  Устройство
![](images/navigatorgui_function_as.png) |  Функция, вид представления "Многополюсный"
![](images/navigatorgui_overviewplacement_as.png) |  Функция, вид представления "Обзор"
![](images/navigatorgui_paircrossreference_as.png) |  Функция, вид представления "Парная перекрестная ссылка"
![](images/navigatorgui_singlepole_as.png) |  Функция, вид представления "Однополюсный"
![](images/navigatorgui_pidiagram_as.png) |  Функция, вид представления "Функциональная схема автоматизации"
![](images/navigatorgui_mountingfunction_as.png) |  Функция, вид представления "Трехмерный чертеж монтажных поверхностей"
![](images/navigatorgui_functional_as.png) |  Функция, вид представления "Функциональный"
![](images/navigatorgui_functionoverviewfluid_as.png) |  Функция, вид представления "Обзор функций (Fluid-Техника)"
![](images/navigatorgui_functiontemplate_as.png) |  Шаблон функции
![](images/navigatorgui_pdnpartplacement_as.png) |  Размещение изделия
![](images/navigatorgui_part_as_15x15.png) |  Изделие
![](images/navigatorgui_assemblyplaced_as.png) |  Изделие узла
![](images/navigatorgui_blackbox_as.png) |  Черный ящик, блок ПЛК
![](images/navigatorgui_shieldingauxfunc_as.png) |  Экранирование
![](images/navigatorgui_cable_as.png) |  Определение кабеля
![](images/navigatorgui_plug_as.png) |  Определение штекера
![](images/navigatorgui_terminal_as.png) |  Определение клеммника
![](images/navigatorgui_partialterminal_as.png) |  Распределенная клемма
![](images/navigatorgui_insulation_as.png) |  Изолированный конец соединения

!!! note "Замечание:"

* Пиктограммы для различных видов представления и для специальных функций (напр., черных ящиков, определений кабеля и т. д.) часто используются в комбинации с другими пиктограммами. Например, стоящая впереди пиктограмма ![](images/navigatorgui_mainfunctionpart_as.png) означает главную функцию (напр., ![](images/navigatorgui_mainfunctionpart_as.png)![](images/navigatorgui_function_as.png) многополюсную главную функцию).
* В навигаторах для отображения устройств все устройства, которые имеют только обозначение устройства, но не структурные идентификаторы, такие как функциональное назначение, место установки и т. д., на уровне структуры дерева сортируются ![](images/navigatorgui_device_as.png) Без структурных идентификаторов. Все устройства, которые имеют собственное ОУ, на уровне структуры дерева сортируются ![](images/navigatorgui_device_as.png) без ОУ.

В следующей таблице перечислены самые важные пиктограммы, которые используются в комбинации с другими пиктограммами.

Пиктограмма |  Значение
---|---
![](images/navigatorgui_mainfunctionpart_as.png) |  Размещенная главная функция (напр., ![](images/navigatorgui_mainfunctionpart_as.png)![](images/navigatorgui_function_as.png) размещенная многополюсная главная функция)
![](images/navigatorgui_nonplacedmainfunction_as.png) |  Неразмещенная главная функция (напр., ![](images/navigatorgui_nonplacedmainfunction_as.png)![](images/navigatorgui_function_as.png) неразмещенная многополюсная главная функция)
![](images/navigatorgui_nonplaced_as_15x15.png) |  Неразмещенная функция / неразмещенный объект (напр., ![](images/navigatorgui_nonplaced_as.png)![](images/navigatorgui_function_as.png) неразмещенная многополюсная функция)
![](images/navigatorgui_overlayedfunction_as.png) |  Наложенный шаблон функции (например, ![](images/navigatorgui_functionstate_as.png) многополюсная функция накладывается на шаблон функции)
![](images/navigatorgui_safety_as.png) |  Защитная функция (напр., ![](images/navigatorgui_functionsafety_as.png) многополюсная защитная функция)
![](images/navigatorgui_protectedfunction_as.png) |  Функция / сегмент с защитой устройства (напр., ![](images/navigatorgui_protectedmainfunction_as.png)![](images/navigatorgui_function_as.png) многополюсная главная функция с защитой устройства)
![](images/navigatorgui_readonlysmall_as.png) |  Функция / сегмент с защитой от изменений (напр., ![](images/navigatorgui_mainfctwriteprotect_as.png)![](images/navigatorgui_function_as.png) многополюсная главная функция с защитой от изменений)
![](images/navigatorgui_message_ls.png) |  Ошибочная функция или ошибочный объект (напр., ![](images/navigatorgui_functionmessage_ls.png) ошибочная многополюсная функция).
Эта пиктограмма после проверки данных проекта показывает, что функция / объект содержит противоречивые или неполные данные.

**См. также:**

* [Особенности навигаторов](userinterface_k_besonderheitennavigatoren.md)
* [Диалоговое окно Пространство листа — <Имя проекта>](cabinetgui_d_navigator.md)
* [Диалоговое окно Предварительное планирование — <Имя проекта>](planninggui_d_navigator.md)
* [Диалоговое окно ПЛК — <Имя проекта>](plcgui_d_spsdaten.md)
* [Диалоговое окно Топология — <Имя проекта>](cablinggui_d_navigator.md)
* [Диалоговое окно Потенциалы - <Имя проекта>](potentialbrowsergui_d_potenziale.md)
* [Диалоговое окно Трубопроводы - <Имя проекта>](potentialbrowsergui_d_rohrleitungen.md)
* [Диалоговое окно Макросы — <Имя проекта>](macrosgui_d_makronavigator.md)
* [Расширения имен файлов и пиктограммы для проектов](projects_k_icons.md)
