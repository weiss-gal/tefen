# מציאת ממוצע

הקוד הבא אמור לקרוא סדרת מספרים עד המילה stop ולחשב את הממוצע שלהם
השתמש בדיבאגר למצוא את הבאג ותקן אותו

```csharp
// Find the maximum number
string inputStr;
int sum = 0;
int count = 0;

Console.WriteLine("Please insert a number:");
inputStr = Console.ReadLine();
count++;
while (inputStr.ToLower() != "stop")
{
    
    int num = int.Parse(inputStr);
    sum += num;
    

    Console.WriteLine("Please insert a number:");
    inputStr = Console.ReadLine();
    count++;
}

double average = (double)sum / count;

Console.WriteLine("The average of the numbers is: " +  average);
```