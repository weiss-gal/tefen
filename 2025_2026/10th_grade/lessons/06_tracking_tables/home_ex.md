# תרגיל בית

בצע טבלת מעקב עבור הקוד הבא, עבור לפחות שלושת הקלטים הבאים:

- 321
- 123
- 2012

הסבר ככל יכולתך מה עושה הקוד


```csharp
Console.Write("Enter integer number: ");
int num = int.Parse(Console.ReadLine());
int result = 0;

while (num > 0)
{
    int digit = num % 10;
    result = result * 10 + digit;

    num = num / 10;
}

Console.Write("Result: " + result);
```

## סעיף בונוס
הוסף לקוד לולאת קלט כך שלא ניתן יהיה להכניס משהו אחר ממספר שלם. הנחיה- השתמש בפונקציה int.tryParse() . ניתן להשתמש באינטרנט כדי לחפש דוגמאות

הנה לינק להסבר באתר הרשמי של מיקרוסופט, שים לב שיש מספר גרסאות לפקודה (פונקציה) הזו, הלינק הוא לגרסה שרלוונטית אלינו:

https://learn.microsoft.com/en-us/dotnet/api/system.int32.tryparse?view=net-9.0#system-int32-tryparse(system-string-system-int32@)
