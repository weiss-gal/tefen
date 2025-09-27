# יצירת מחרוזות מתקדמת

## חומרים לשיעור

- מצגת של הילה קדמן בנושא פלט. עמודים 38 עד 47

לינק למצגת: [מצגת המרות](https://drive.google.com/file/d/1AZQmVzFuO1SEvWSKUj5luib_OA3Da-Ny/view)

## מה נלמד היום?

עד עכשיו כשרצינו להדפיס מספר משתנים, היינו צריכים לכתוב הרבה שורות או לחבר מחרוזות עם הסימן `+`.  
היום נלמד שתי שיטות חכמות יותר ליצירת הודעות מורכבות.

## הבעיה - הדפסה "מסובכת"

נניח שיש לנו שני מספרים ואנחנו רוצים להדפיס אותם יחד עם הודעה:

```csharp
int num1 = 15;
int num2 = 27;

// The old and complicated way
Console.WriteLine("The two numbers are: " + num1 + " and " + num2);
```

זה עובד, אבל זה לא נוח וקשה לקרוא. בואו נלמד דרכים טובות יותר!

## שיטה ראשונה: Formatted Output עם Placeholders

### איך זה עובד?
במקום לחבר מחרוזות עם `+`, אנחנו כותבים **ממלא מקום** (placeholder) במחרוזת עם המספרים `{0}`, `{1}`, `{2}` וכו'.  
אחר כך אנחנו מעבירים את המשתנים כפרמטרים נוספים ל־`Console.WriteLine`.

### התחביר:
```csharp
Console.WriteLine("The string with {0} and {1}", first_variable, second_variable);
```

### דוגמה:
```csharp
int num1 = 15;
int num2 = 27;

Console.WriteLine("The two numbers are: {0} {1}", num1, num2);
```

**התוצאה:** `The two numbers are: 15 27`

### עוד דוגמאות:
```csharp
string name = "Danny";
int age = 16;
double height = 1.75;

Console.WriteLine("Hello {0}! You are {1} years old and {2} meters tall", name, age, height);
// Output: Hello Danny! You are 16 years old and 1.75 meters tall

Console.WriteLine("Calculation: {0} + {1} = {2}", 5, 3, 5+3);
// Output: Calculation: 5 + 3 = 8
```

### חשוב לזכור:
- **{0}** הוא המשתנה הראשון שאחרי המחרוזת
- **{1}** הוא המשתנה השני
- **{2}** הוא המשתנה השלישי, וכן הלאה...

## שיטה שנייה: Interpolated Strings (המחרוזות החדשות!)

החל מגרסת Visual Studio 2017, C# תומכת בשיטה חדשה ונוחה עוד יותר שנקראת **Interpolated Strings**.

### איך זה עובד?
1. אנחנו מתחילים את המחרוזת עם הסימן `$`
2. אנחנו כותבים את שמות המשתנים או חישובים ישירות בתוך `{}`

### התחביר:
```csharp
Console.WriteLine($"The string with {variable1} and {variable2}");
```

### דוגמה:
```csharp
int num1 = 15;
int num2 = 27;

Console.WriteLine($"The two numbers are: {num1} {num2}");
```

**התוצאה:** `The two numbers are: 15 27`

### עוד דוגמאות:
```csharp
string name = "Sarah";
int age = 17;
double grade = 95.5;

Console.WriteLine($"Student {name} is {age} years old and got grade {grade}");
// Output: Student Sarah is 17 years old and got grade 95.5

// You can also perform calculations inside the {}:
int a = 10;
int b = 5;
Console.WriteLine($"{a} + {b} = {a + b}");
// Output: 10 + 5 = 15

Console.WriteLine($"{a} × {b} = {a * b}");
// Output: 10 × 5 = 50
```

## השוואה בין השיטות

נסתכל על דוגמה שמראה את שלוש הדרכים:

```csharp
string studentName = "Avi";
int mathGrade = 85;
int englishGrade = 92;

// Method 1: String concatenation (old way)
Console.WriteLine("Student " + studentName + " got " + mathGrade + 
                  " in math and " + englishGrade + " in English");

// Method 2: Formatted Output
Console.WriteLine("Student {0} got {1} in math and {2} in English", 
                  studentName, mathGrade, englishGrade);

// Method 3: Interpolated Strings (most convenient!)
Console.WriteLine($"Student {studentName} got {mathGrade} in math and {englishGrade} in English");
```

**כל שלושת הקודים יתנו את אותה תוצאה:**  
`Student Avi got 85 in math and 92 in English`

## מתי להשתמש באיזו שיטה?

- **Interpolated Strings** (`$"..."`) - **המומלצת!** הכי קל לקרוא ולכתוב
- **Formatted Output** (`{0}, {1}...`) - טובה כשיש הרבה משתנים חוזרים
- **חיבור מחרוזות** (`+`) - רק במקרים פשוטים מאוד

## דוגמה מעשית: מחשבון פשוט

```csharp
Console.WriteLine("Enter first number:");
int num1 = int.Parse(Console.ReadLine());

Console.WriteLine("Enter second number:");
int num2 = int.Parse(Console.ReadLine());

// Using Interpolated Strings:
Console.WriteLine($"Calculation results:");
Console.WriteLine($"{num1} + {num2} = {num1 + num2}");
Console.WriteLine($"{num1} - {num2} = {num1 - num2}");
Console.WriteLine($"{num1} × {num2} = {num1 * num2}");
Console.WriteLine($"{num1} ÷ {num2} = {(double)num1 / num2}");
```

## תרגיל לתרגול

נסו לכתוב תכנית שמבקשת מהמשתמש:
1. שם
2. גיל  
3. ציון בבחינה

והיא מדפיסה הודעה נחמדה עם כל הפרטים באמצעות **Interpolated Strings**.

דוגמה לפלט:
```
Hello Rachel! You are 16 years old and got an excellent grade: 94!
```
