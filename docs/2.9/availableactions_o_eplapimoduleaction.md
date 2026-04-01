# Операция: EplApiModuleAction

**Параметр** |  **Описание**
---|---
register  |  Полное имя регистрируемого DLL-файла Add-in.
unregister  |  Полное имя Add-in, регистрация которого отменяется.
unregisterInternal  |  Полное имя Add-in, регистрация которого отменяется. Если модуль не может быть выгружен из-за ошибки, то выполняется только отмена его регистрации.

!!! example "Пример:"

    Вызов операции для загрузки Add-in:W3u.exe EplApiModuleAction
/register:"C:\...\EPLAN\Electric P8\...\Bin\Eplan.EplAddin.MyAddin3.dll"Вызов операции для выгрузки дополнительного модуля:W3u.exe EplApiModuleAction
/unregister:"Eplan.EplAddin.MyAddin3"

С вашей помощью мы можем улучшить работу системы. Мы документируем ваши действия в Google Analytics, чтобы постоянно совершенствовать справочную систему ([Дополнительная информация и возможности подачи возражений](helpsystem_hinweise_optout.md)).

Скрыть сообщение
