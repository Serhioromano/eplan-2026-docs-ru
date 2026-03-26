


[](EPLAN_Help_k_start.htm)

  * placeholder



  * Все файлы






Эта функциональность предусмотрена только в определенных модулях расширения. [Информация / авторское право](license_k_start.htm)

Вы находитесь здесь:

## Операция: EplApiModuleAction

  
**Параметр** |  **Описание**  
---|---  
register  |  Полное имя регистрируемого DLL-файла Add-in.   
unregister  |  Полное имя Add-in, регистрация которого отменяется.  
unregisterInternal  |  Полное имя Add-in, регистрация которого отменяется. Если модуль не может быть выгружен из-за ошибки, то выполняется только отмена его регистрации.  


!!! example "Пример:"

    Вызов операции для загрузки Add-in:W3u.exe EplApiModuleAction 
/register:"C:\...\EPLAN\Electric P8\...\Bin\EPLAN.EplAddin.MyAddin3.dll"Вызов операции для выгрузки дополнительного модуля:W3u.exe EplApiModuleAction 
/unregister:"Eplan.EplAddin.MyAddin3"


 
