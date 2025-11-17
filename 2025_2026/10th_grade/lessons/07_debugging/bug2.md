# מציאת מקסימום

הקוד הבא אמור לקבל  סדרת מספרים עד המילה stop ומציג את המספר המקסימלי
בעזרת הדיבאגר, מצא את הבאג ותקן אותו

```csharp
// Find the maximum number
string inputStr;
int max = 0;

Console.WriteLine("Please insert a number:");
inputStr = Console.ReadLine();
while (inputStr.ToLower() != "stop")
{
    
    int num = int.Parse(inputStr);
    if (num < max)
    {
        max = num;
    }

    Console.WriteLine("Please insert a number:");
    inputStr = Console.ReadLine();
}

Console.WriteLine("The maximum number read is: " +  max);
```