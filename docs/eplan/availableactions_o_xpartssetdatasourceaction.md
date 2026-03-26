
  
  
[](EPLAN_Help_k_start.htm)

  * placeholder



  * Все файлы






Эта функциональность предусмотрена только в определенных модулях расширения. [Информация / авторское право](license_k_start.htm)

Вы находитесь здесь:

## Операция: XPartsSetDataSourceAction

  
**Параметр** |  **Описание**  
---|---  
DataSourceType |  Тип источника базы данных (0 = база данных Eplan (значение по умолчанию), 1 = сервер SQL, 3 = коллекция eStock).  
DataBaseFileName |  Имя базы данных с полным путем к файлу.  
SqlServer |  Имя сервера SQL.  
SqlCatalog |  Имя базы данных SQL.  
SqlUserName |  Имя пользователя.  
SqlPassword |  Пароль пользователя.  
SqlLogin |  Вход в SQL (0 = реестр Windows (значение по умолчанию), 1 = реестр сервера SQL (имя пользователя + пароль)).  
SqlFullName |  Полное имя сервера SQL. Не может использоваться вместе с одним из параметров SqlServer, SqlCatalog, SqlUserName или SqlPassword.  
CollectionName |  Имя коллекции eStock.  
CollectionId |  Идентификатор коллекции eStock.  


!!! note "Замечание:"

    


 

!!! example "Пример:"

    Задает базу данных Eplan в качестве источника базы данных:XPartsSetDataSourceAction 
/DataSourceType:0 
/DataBaseFileName:C:\Users\Public\EPLAN\Data\Article\COMPANY_NAME\Database.alkЗадает сервер SQL в качестве источника базы данных с регистрацией Windows при входе в систему:XPartsSetDataSourceAction 
/DataSourceType:1 
/SqlLogin:0 
/SqlServer:SQL_SERVER_NAME 
/SqlCatalog:SQL_DATABASEЗадает сервер SQL в качестве источника базы данных с регистрацией сервера SQL при входе в систему:XPartsSetDataSourceAction 
/DataSourceType:1 
/SqlLogin:1 
/SqlServer:SQL_SERVER_NAME 
/SqlCatalog:SQL_DATABASE 
/SqlUserName:SQL_USERNAME 
/SqlPassword:SQL_PASSWORDЗадает сервер SQL в качестве источника базы данных с регистрацией сервера SQL при входе в систему. При этом для сервера SQL указывается полное имя:XPartsSetDataSourceAction 
/DataSourceType:1 
/SqlLogin:1 
/SqlFullName:SQL_SERVER_NAME|SQL_DATABASE|2|SQL_USERNAME|SQL_PASSWORDЗадает коллекцию eStock в качестве источника базы данных:XPartsSetDataSourceAction 
/DataSourceType:3 
/CollectionName:ESTOCK_COLLECTION_NAME 
/CollectionId:ESTOCK_COLLECTION_ID


 
