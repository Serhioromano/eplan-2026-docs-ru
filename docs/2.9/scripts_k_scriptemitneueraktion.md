# Сценарии с новыми операциями

В EPLAN можно [загрузить](Glossary_o_laden.md) и [выгрузить](Glossary_o_entladen.md) сценарий. В таком случае функция запуска не выполняется, а в EPLAN регистрируются специальные [функции](Glossary_o_funktionen.md). В EPLAN можно добавить новую операцию или пункт меню, или зарегистрировать функции, чтобы реагировать на специальные результаты EPLAN.

Чтобы программе добавить новую операцию, функция в [сценарии](Glossary_o_scripte.md) обозначается через атрибут [DeclareAction]. С помощью параметра атрибута [DeclareAction()] задайте имя новой операции в EPLAN.

Общая структура соответствующего сценария C# выглядит так:

    public class <ScriptName>
    {

         [DeclareAction("<ActionName>")]
         public void <FunctionName>
         {

               //<Enter your code text here>
               return;

         }

    }

!!! example "Пример:"

    Следующий пример демонстрирует сценарий на C#, который регистрирует операцию:public class SimpleScriptAction
{

     [DeclareAction("MyScriptAction")]
     public void MyFunctionAsAction()
     {

           MessageBox.Show("MyFunctionAsAction was called!", "RegisterScriptAction");
           return;

     }

}При загрузке сценария с вышеприведенным кодом функцияMyFunctionAsActionрегистрируется в EPLAN как операция с именемMyScriptAction.Аналогичный пример в Visual Basic.Net выглядит следующим обр.:Public Class SimpleScriptAction

     <DeclareAction("MyScriptAction")> _
     Public Sub MyFunctionAsAction()

           MessageBox.Show("MyFunctionAsAction was called!", "RegisterScriptAction")
           Return

     End Sub 'MyFunctionAsAction

End Class 'SimpleScriptAction

После того как загружен соответствующий сценарий (с [DeclareAction]) через пункт меню Загрузить, новая операция может использоваться в EPLAN как любая другая операция. Можно, например, вызвать через командную строку или добавить ее к пункту меню или кнопке на [панели инструментов](Glossary_o_symbolleisten.md).

Если сценарий загружен один раз, при следующем запуске EPLAN он загружается автоматически, и операция снова доступна. Отмена такого сценария выполняется через пункт меню Выгрузить.

**См. также:**

* [Сценарии](scripts_k_start.md)
* [Выполнить или загрузить сценарии](scripts_h_scripteausfuehren.md)
С вашей помощью мы можем улучшить работу системы. Мы документируем ваши действия в Google Analytics, чтобы постоянно совершенствовать справочную систему ([Дополнительная информация и возможности подачи возражений](helpsystem_hinweise_optout.md)).

Скрыть сообщение
