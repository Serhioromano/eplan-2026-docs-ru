## Операция: plcservice

  
**Параметр** |  **Описание**  
---|---  
TYPE |  Вид задачи, которую должна выполнить операция:  
BUSDATAEXPORT: Экспортировать данные ПЛК.  
BUSDATAIMPORT: Импортировать данные ПЛК. GENERATEPLCSCHEMATIC: Генерировать схему соединений. EXPORTADDRESSOVERVIEW: Экспортировать адреса / списки присвоения.  
PROJECTNAME |  Имя проекта с полным путем к файлу.  
  
LANGUAGE |  Код языка. Этот параметр оказывает влияние, только когда параметр TYPE имеет одно из следующих значений: BUSDATAEXPORT, BUSDATAIMPORT.  
CONVERTERID |  Идентификатор для программ конфигурации ПЛК. Возможные значения:

* PlcDcExchangerBeckhoffTC3AML: Beckhoff TwinCAT 3 (AR APC 1.1.0)
* PlcDcExchangerBoschAML: Bosch Nexeed Automation (AR APC 1.0.0)
* PlcDcExchangerLogiCals3AML: logi.cals logi.CAD 3 (AR APC 1.1.0)
* PlcDcExchangerMitsubishiAML: Mitsubishi iQ Works (AR APC 1.0.0)
* PlcDcExchangerMitsubishi110AML: Mitsubishi iQ Works (AR APC 1.1.0)
* PlcDcExchangerPhoenixContactAML: Phoenix Contact PLCnext Engineer 2019 (AR APC 1.0.0)
* PlcDcExchangerRockwellArchitectAML: Rockwell Automation Studio 5000 (AR APC 1.0.0)
* PlcDcExchangerSiemensTIA15AML: Siemens SIMATIC STEP 7 TIA-Portal 15 (AR APC 1.0.0)
* PlcDcExchangerSiemensTIA151AML: Siemens SIMATIC STEP 7 TIA Portal 15.1 (AR APC 1.0.0)
* PlcDcExchangerSiemensTIA16AML: Siemens SIMATIC STEP 7 TIA Portal 16 (AR APC 1.1.0)
* PlcDcExchangerSiemensTIA17AML: Siemens SIMATIC STEP 7 TIA Portal 17 (AR APC 1.2.0)
* PlcDcExchangerSiemensTIA18AML: Siemens SIMATIC STEP 7 TIA Portal 18 (AR APC 1.3.0)
* PlcDcExchangerSiemensTIA19AML: Siemens SIMATIC STEP 7 TIA Portal 19 (AR APC 1.4.0)
* PlcDcExchangerSiemensTSTAML: Siemens TIA Selection Tool (AR APC 1.1.0)
* PlcDcAMLExchangerGeneral: Стандартный формат обмена ПЛК (AutomationML)
* PlcDcXMLExchangerABB: ABB Automation Builder
* PlcDcXMLExchangerBandR: B and R Automation Studio
* PlcDcXMLExchangerRexroth: Bosch Rexroth Indra Works
* PlcDcXMLExchangerSchneider: Schneider Unity Pro XL
* PlcDcXMLExchangerSiemens: Siemens SIMATIC STEP 7 5.6
* PlcDcXMLExchangerUniversal: Стандартный формат обмена ПЛК.

Этот параметр оказывает влияние, только когда параметр TYPE имеет одно из следующих значений: BUSDATAEXPORT, BUSDATAIMPORT.  
CONFIGURATIONPROJECT |  Название проекта конфигурации ПЛК, который необходимо экспортировать. Этот параметр оказывает влияние, только когда параметр TYPE имеет одно из следующих значений: BUSDATAEXPORT, EXPORTADDRESSOVERVIEW  
DESTINATIONFILE |  Целевой файл для экспорта данных. Этот параметр оказывает влияние, только когда параметр TYPE имеет одно из следующих значений: BUSDATAEXPORT, EXPORTADDRESSOVERVIEW  
SOURCEFILE |  Исходный файл для импорта данных. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: BUSDATAIMPORT.  
OVERWRITE |  Если целевой файл уже существует, этот параметр указывает, нужно ли этот файл перезаписать (0 = нет, 1 = да).  
Значение по умолчанию: 0 Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: BUSDATAEXPORT.  
FORMAT |  Формат файла экспорта (необязательно). Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: BUSDATAEXPORT.  
EXPORTPORTSPECIFICINTERCONNECTION |  Экспортировать подробное соединение портов (необязательно). Возможные значения: 0 = нет, 1 = да. Если этот параметр не используется, то значение по умолчанию будет таким же, как указано в текущий момент в интерфейсе пользователя. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: BUSDATAEXPORT.  
EXPORTACCESSORIES |  Экспортировать принадлежности (необязательно). Возможные значения: 0 = нет, 1 = да. Если этот параметр не используется, то значение по умолчанию будет таким же, как указано в текущий момент в интерфейсе пользователя. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: BUSDATAEXPORT.  
EXPORTDRIVES |  Экспортировать приводы (необязательно). Возможные значения: 0 = нет, 1 = да. Если этот параметр не используется, то значение по умолчанию будет таким же, как указано в текущий момент в интерфейсе пользователя. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: BUSDATAEXPORT.  
EXPORTDEVICESPECIFICCONFIGURATIONVALUES |  Экспортировать значения конфигурации, связанные с устройствами: (необязательно). Возможные значения: 0 = нет, 1 = да. Если этот параметр не используется, то значение по умолчанию будет таким же, как указано в текущий момент в интерфейсе пользователя. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: BUSDATAEXPORT.  
IMPORTMATCH |  Параметры синхронизации при импорте данных ПЛК. Процесс импорта синхронизирует импортируемые объекты с объектами, имеющимися в проекте. В зависимости от выбранного параметра поиск совпадений выполняется на основе внутренних ид. объекта или идентифицирующих названий объектов. Если импортируемый объект подходит к имеющейся функции, свойства имеющейся функции обновляются, а для объектов, не имеющих соответствия, в проекте генерируется новая функция. Возможные параметры:

* 0: Синхронизация на основе внутренних ид. объектов.
* 1: Синхронизация на основе идентифицирующих имен. Обратите внимание, что в этом случае может открыться диалоговое окно синхронизации, где нужно отдельно выбрать функцию для обновления.
* 2: Без синхронизации, для всех импортируемых объектов генерируются новые функции.

Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: BUSDATAIMPORT.  
CONFIGFILE |  Путь файла конфигурации для генерирования схемы соединений. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: GENERATEPLCSCHEMATIC.  
SINGLELINEPAGES |  Если указан этот параметр, генерируются однополюсные страницы (0 = нет, 1 = да).  
Значение по умолчанию: 0   
Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: GENERATEPLCSCHEMATIC.  
MULTILINEPAGES |  Если указан этот параметр, генерируются многополюсные страницы (0 = нет, 1 = да).  
Значение по умолчанию: 0   
Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: GENERATEPLCSCHEMATIC.  
OVERVIEWS |  Если указан этот параметр, генерируются обзорные страницы (0 = нет, 1 = да).  
Значение по умолчанию: 0   
Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: GENERATEPLCSCHEMATIC.  
RACKOVERVIEWS |  Если указан этот параметр, генерируются обзорные страницы каркасов (0 = нет, 1 = да).  
Значение по умолчанию: 0   
Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: GENERATEPLCSCHEMATIC.  
PLCSTATION |  Имя рабочей станции ПЛК, которую необходимо экспортировать. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: EXPORTADDRESSOVERVIEW  
PLCCPU |  Имя ЦПУ, которое необходимо экспортировать. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: EXPORTADDRESSOVERVIEW  

!!! example "Пример:"

    Экспортировать данные ПЛК:plcservice 
/TYPE:BUSDATAEXPORT 
/CONFIGURATIONPROJECT:Schneider-Electric 
/DESTINATIONFILE:"C:\tempdir\plcservice_export_1.xef" 
/PROJECTNAME:"C:\Users\Public\EPLAN\Projects\EPLAN_Sample_Project.elk" 
/LANGUAGE:de_DE 
/CONVERTERID:PlcDcXMLExchangerSchneider 
/OVERWRITE:1Импортировать данные ПЛК:plcservice 
/TYPE:BUSDATAIMPORT 
/SOURCEFILE:"C:\tempdir\plcservice_export_2.xml" 
/PROJECTNAME:"C:\Users\Public\EPLAN\Projects\EPLAN_Sample_Project.elk" 
/LANGUAGE:de_DE 
/CONVERTERID:PlcDcXMLExchangerUniversalГенерировать схему соединений:plcservice 
/TYPE:GENERATEPLCSCHEMATIC 
/PROJECTNAME:"C:\Users\Public\EPLAN\Projects\EPLAN_Sample_Project.elk" 
/CONFIGFILE:"C:\tempdir\schematics_generation_config.xml" 
/SINGLELINEPAGES:1 
/MULTILINEPAGES:1Экспортировать адреса / списки присвоения:plcservice 
/TYPE:EXPORTADDRESSOVERVIEW 
/PROJECTNAME:"C:\Users\Public\EPLAN\Electric P8\Projects\Microsoft\EPLAN_Sample_Project.elk" 
/CONFIGURATIONPROJECT:"CAx_AML_Drive_00" 
/PLCSTATION:"S71500/ET200MP station_1" 
/PLCCPU:"1" 
/DESTINATIONFILE:"c:\tempdir\address_overview_export.csv"

 
