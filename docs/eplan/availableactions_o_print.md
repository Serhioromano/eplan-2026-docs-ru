


[](EPLAN_Help_k_start.htm)

  * placeholder



  * Все файлы






Эта функциональность предусмотрена только в определенных модулях расширения. [Информация / авторское право](license_k_start.htm)

Вы находитесь здесь:

## Операция: print

  
**Параметр** |  **Описание**  
---|---  
TYPE |  Вид выполняемой задачи:  
PROJECT: Выводит на печать проект.  
PAGES: Печатает страницы.  
PROJECTNAME |  Имя проекта с полным путем файла (является опцией).  
Если не задано, то выбранный проект используется, когда операция вызывается через интерфейс пользователя (например, через сценарий или ленту). При вызове из командной строки Windows следует определить PROJECTNAME или сначала следует использовать ProjectAction. В противном случае отобразится системное сообщение.  
PRINTERNAME |  Имя принтера (необязательно).  
Значение по умолчанию: Заданный на вашем компьютере принтер.  
PAGENAME |  Распечатываемая страница (необязательно).  
PRINTCOLLATE |  Сортирует (необязательно, 0 = Нет, 1 = Да).  
Значение по умолчанию: 1  
PRINTREVERSE |  Обратный порядок (необязательно, 0 = Нет, 1 = Да).  
Значение по умолчанию: 0  
NUMBER |  Число распечаток.  
Значение по умолчанию: 1  
DESTINATIONFILE |  Путь файла и имя файла вывода.  
Значение по умолчанию: настроенный или указанный принтер  
USEPAGEFILTER |  Определяет, должны ли использоваться только отфильтрованные страницы или все страницы проекта (необязательно). Значение по умолчанию: 0  
PRINTCHANGEDPAGES |  Печатать только измененные страницы  


!!! note "Замечание:"

    


 

!!! example "Пример:"

    Печатать страницу:print 
/TYPE:PAGES 
/PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk 
/PAGENAME:=EB3+ET1/2 
/PRINTERNAME:my_printer 
/NUMBER:2Печатать страницу в файл:print 
/TYPE:PAGES 
/PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk 
/PRINTCOLLATE:0 
/PRINTREVERSE:1 
/DESTINATIONFILE:C:\temp\EPLAN_print.prn 
/USEPAGEFILTER:1Печатать проект:print 
/TYPE:PROJECT 
/PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk 
/PRINTCOLLATE:0 
/PRINTREVERSE:1 
/DESTINATIONFILE:C:\temp\EPLAN_print.prn


 
