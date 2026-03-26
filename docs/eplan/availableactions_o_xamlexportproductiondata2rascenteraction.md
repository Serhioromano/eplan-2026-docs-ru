## Операция: XAMlExportProductionData2RASCenterAction

**Параметр** |  **Описание**  
---|---  
ProjectPath |  Проект, который необходимо экспортировать. Обратите внимание, что этот проект должен быть предварительно открыт на платформе Eplan. Если ничего не указано, будет использоваться текущий проект.  
FileName |  Полный путь и имя файла, который необходимо экспортировать. Если ничего не указано, отображается диалоговое окно.  
DatabaseId |  Идентификатор проекта для проекта (является опцией).  
Без ввода используется параметр ProjectPath.  
WholeProject |  Укажите, будет ли экспортироваться весь проект или только выбранные объекты (необязательно).  
ConfigScheme |  Схема конфигурации (необязательно). Значение по умолчанию: последняя использованная схема конфигурации.  

!!! note "Замечание:"

    Если файл, используемый в параметреFileName, уже существует, появится диалоговое окно с вопросом о том, следует ли перезаписать файл.

!!! example "Пример:"

    XAMlExportProductionData2RASCenterAction 
/ProjectPath:C:\Projects\EPLAN\EPLAN_Sample_Project.elk 
/FileName:C:\Exports\EPLAN\EPLAN_Sample_Project.amlXAMlExportProductionData2RASCenterAction 
/DatabaseId:27 
/FileName:C:\Exports\EPLAN\EPLAN_Sample_Project.aml

