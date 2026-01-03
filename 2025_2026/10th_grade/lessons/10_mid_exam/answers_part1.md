## שאלות לדוגמה – פתרונות

### CountEvenDigits

כתבו פעולה סטטית שתחזיר כמה ספרות במספר הן זוגיות.

```csharp
public static int CountEvenDigits(int num)
{
    int count = 0;

    while (num > 0)
    {
        int digit = num % 10;
        if (digit % 2 == 0)
            count++;

        num = num / 10;
    }

    return count;
}
```

---

### CountAbove

```csharp
public static int CountAbove(int num, int limit)
{
    int count = 0;

    while (num > 0)
    {
        int digit = num % 10;
        if (digit > limit)
            count++;

        num = num / 10;
    }

    return count;
}
```

---

### IsIncreasing

```csharp
public static bool IsIncreasing(int a, int b, int c)
{
    return a < b && b < c;
}
```

---

## שאלות ידע לדוגמה – תשובות

### Question 1

```csharp
(x > 5) || (y < 10)
```

✅ **Yes**

---

### Question 2

```csharp
(a > 2) && (b % 2 == 1)
```

❌ **No**

---

### Question 3

```csharp
if (x < 3)
    Console.WriteLine("A");
```

❌ **No**

---

### Question 4

```csharp
x = x / 3;
```

✅ **3**

---

### Question 5

```csharp
while (i < 5)
{
    i++;
}
```

✅ **Yes**

---

### Question 6

```csharp
while (i < 10)
{
    i = i + 3;
}
```

❌ **No**

---

### Question 7

```csharp
x % 7 == 0
```

✅ **Yes**

---

### Question 8

```csharp
for (int i = 1; i <= 3; i++)
{
    sum = sum + i;
}
```

✅ **Yes**

---

### Question 9

```csharp
isEven(9)
```

❌ **No**

---

### Question 10

```csharp
x + 2 * 3 == 18
```

❌ **No**