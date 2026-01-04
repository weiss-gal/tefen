# הכנה למבחן אמצע

## דוגמא למבחן בגרות מקיץ 2025

בלינק הבא תוכלו למצוא עותק של מבחן בגרות. לפני שאתם עוברים עליו, קחו בחשבון שבשלב זה אתם עדיין לא מכירים את כל הפקודות והמושגים כדי לפתור את כל התרגילים. 
עם זאת, כדאי לעבור על המבחן ולהבין כיצד הוא בנוי ולהתרגל לשפה ולדרישות.
[שאלון קיץ 2025](899371_summer_2025.pdf)

במבחן הספציפי הזה אתם כבר יכולים לפתור את שאלות 3 ו6

# שאלות לדוגמא

## countEvenDigits

כתבו פעולה סטטית שתחזיר כמה ספרות במספר הן זוגיות. הפונקציה תקבל מספר שלם כלשהו ותחזיר את מספר הספרות הזוגיות. 

לדוגמא
- עבור המספר 111 הפונקציה תחזיר 0
- עבור המספר 121 הפונקציה תחזיר 1
- עבור המספר 1000122 הפונקציה תחזיר 5

שם הפונקציה: CountEvenDigits

מבנה
```csharp
public static int CountEvenDigits(int num)
{
    // Add your code here
}
```

## CountAbove

כתבו פעולה חיצונית סטטית ששמה
CountAbove

```csharp
public static int CountAbove(int num, int limit)
```

הפעולה מקבלת:

מספר שלם חיובי num

מספר שלם limit

הפעולה תחזיר כמה ספרות במספר num גדולות מ־limit.

דוגמאות:

עבור num = 58394 ו־limit = 5 הפעולה תחזיר 2
(הספרות 8 ו־9)

עבור num = 1111 ו־limit = 3 הפעולה תחזיר 0

עבור num = 709 ו־limit = 6 הפעולה תחזיר 2
(הספרות 7 ו־9)

הניחו שהקלט תקין.

## IsIncreasing

כתבו פעולה חיצונית סטטית ששמה
isIncreasing

```csharp
public static bool IsIncreasing(int a, int b, int c)
```

הפעולה מחזירה true אם המספרים מתקבלים בסדר עולה ממש
(כל מספר גדול מהקודם לו), אחרת מחזירה false.

דוגמאות:

IsIncreasing(2, 5, 9) → true

IsIncreasing(2, 2, 5) → false

IsIncreasing(9, 5, 2) → false

# שאלות ידע לדוגמא (אין בבגרות)

## Question 1
Given:
```csharp
int x = 4;
int y = 7;
```

Does the following expression evaluate to `true`?

```csharp
(x > 5) || (y < 10)
```

- ☐ Yes  
- ☐ No  

---

## Question 2
Given:
```csharp
int a = 3;
int b = 6;
```

Does the following expression evaluate to `true`?

```csharp
(a > 2) && (b % 2 == 1)
```

- ☐ Yes  
- ☐ No  

---

## Question 3
Given the following code:

```csharp
int x = 5;

if (x < 3)
    Console.WriteLine("A");
```

Will anything be printed to the screen?

- ☐ Yes  
- ☐ No  

---

## Question 4
Given:
```csharp
int x = 10;
```

What will be the value of `x` after the following line executes?

```csharp
x = x / 3;
```

- ☐ 3  
- ☐ 3.3  
- ☐ 4  

---

## Question 5
Given the following code:

```csharp
int i = 0;

while (i < 5)
{
    i++;
}
```

At the end of the loop, is the value of `i` equal to 5?

- ☐ Yes  
- ☐ No  

---

## Question 6
Given:
```csharp
int i = 2;

while (i < 10)
{
    i = i + 3;
}
```

Does the loop body execute more than two times?

- ☐ Yes  
- ☐ No  

---

## Question 7
Given:
```csharp
int x = 14;
```

Does the following expression evaluate to `true`?

```csharp
x % 7 == 0
```

- ☐ Yes  
- ☐ No  

---

## Question 8
Given:
```csharp
int sum = 0;

for (int i = 1; i <= 3; i++)
{
    sum = sum + i;
}
```

Is the final value of `sum` equal to 6?

- ☐ Yes  
- ☐ No  

---

## Question 9
Given the following function:

```csharp
public static bool isEven(int num)
{
    return num % 2 == 0;
}
```

Does the following call return `true`?

```csharp
isEven(9)
```

- ☐ Yes  
- ☐ No  

---

## Question 10
Given:
```csharp
int x = 4;
```

Does the following expression evaluate to `true`?

```csharp
x + 2 * 3 == 18
```

- ☐ Yes  

- ☐ No  
