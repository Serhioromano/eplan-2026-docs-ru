## Сценарии с новыми операциями

В Eplan можно загрузить и выгрузить сценарий. В таком случае функция запуска не выполняется, а в Eplan регистрируются специальные функции. В Eplan можно добавить новую операцию или команду, или зарегистрировать функции, чтобы реагировать на специальные события Eplan.

Чтобы программе добавить новую операцию, функция в сценарии обозначается через атрибут [DeclareAction]. С помощью параметра атрибута [DeclareAction()] задайте имя новой операции в Eplan.

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

}При загрузке сценария с вышеприведенным кодом функцияMyFunctionAsActionрегистрируется в Eplan как операция с именемMyScriptAction.Аналогичный пример в Visual Basic.Net выглядит следующим обр.:Public Class SimpleScriptAction

     <DeclareAction("MyScriptAction")> _
     Public Sub MyFunctionAsAction()

           MessageBox.Show("MyFunctionAsAction was called!", "RegisterScriptAction")
           Return

     End Sub 'MyFunctionAsAction

End Class 'SimpleScriptAction

 

После загрузки соответствующего сценария (при помощи [DeclareAction]) командой Загрузить (командный путь: Файл > Дополнительно > группа команд Расширения > Интерфейсы > группа команд Сценарии > Загрузить) можно использовать новую операцию так же как любую другую операцию в Eplan. Ее можно, например, вызвать через командную строку или добавить к команде в ленте.

Если сценарий загружен один раз, при следующем запуске Eplan он загружается автоматически, и операция снова доступна. Отмена регистрации такого сценарии выполняется в виде Backstage Дополнительно с помощью команды Выгрузить.

См. также

[Сценарии](eplan/scripts_k_start.md)

[Выполнить или загрузить сценарии](eplan/scripts_h_scripteausfuehren.md)
