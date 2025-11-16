# תרגיל 3 - טבלת מעקב

בצע טבלת מעקב לקוד הבא. עבור הקלטים הבאים:

- 1,2,3
- 3,2,1
- 1,3,2

והסבר מה מטרת הקוד

```csharp
Console.Write("Enter num1: ");
int num1 = int.Parse(Console.ReadLine());

Console.Write("Enter num2: ");
int num2 = int.Parse(Console.ReadLine());

Console.Write("Enter num3: ");
int num3 = int.Parse(Console.ReadLine());

int tmp;

// Pass 1: compare 1 ↔ 2
if (num1 > num2)
{
    tmp = num1;
    num1 = num2;
    num2 = tmp;
}

// Pass 2: compare 2 ↔ 3
if (num2 > num3)
{
    tmp = num2;
    num2 = num3;
    num3 = tmp;
}

// Pass 3: compare 1 ↔ 2 again
if (num1 > num2)
{
    tmp = num1;
    num1 = num2;
    num2 = tmp;
}

Console.WriteLine("Result: " + num1 + ", " + num2 + ", " + num3);
```