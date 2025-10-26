# משפט תנאי מורכב

מצגת רלוונטית: 
[משפט תנאי מורכב, עמוד 5 עד 31](https://drive.google.com/file/d/1sQ2w0r5qevaDh9YsmCyUni_z6ALmLVbW/view)

פרק משפטי תנאי בקמפוס IL:
(https://app.campus.gov.il/learning/course/course-v1:MoE+EDU_Matric_ComputerScienceA_HE+2023_1/block-v1:MoE+EDU_Matric_ComputerScienceA_HE+2023_1+type@sequential+block@7594d368001146dda5560ad2d5b7db04)[לינק לפרק - דורש הרשמה באמצעות גוגל או מייל]

סרטון על שימוש בIF: 
(https://www.youtube.com/watch?v=Jth2EptHSlE&t=5s)[לינק לסרטון]

סרטון על שימוש בAND:
(https://www.youtube.com/watch?v=dvevjy6wkuU)[לינק לסרטון]


סרטון על שימוש בOR:
(https://youtu.be/fygYdpb9wOI?si=ChFcFQU8pKvsBbQT)[לינק לסרטון]

## אופרטורים לוגיים 

### אופרטור AND (`&&`)

אופרטור **AND** (ב־C# נכתב `&&`) מאפשר לבדוק ששני תנאים מתקיימים **בו־זמנית**.

לדוגמה:

```csharp
int number = 8;

if (number > 0 && number < 10)
{
    Console.WriteLine("The number is between 1 and 9.");
}
```

### אופרטור OR (`||`)

אופרטור **OR** (נכתב `||`) מחזיר אמת אם **לפחות אחד** מהתנאים נכון.

לדוגמה:

```csharp
int number = 10;

if (number < 0 || number > 5)
{
    Console.WriteLine("The number is outside the range 0–5.");
}
```

## טבלת קדימות והשוואה של אופרטורים לוגיים והשוואתיים

| רמה | סוג | אופרטור | שם באנגלית | תיאור | דוגמה | תוצאה |
|:---:|:----|:---------|:-------------|:--------|:--------|:---------|
| 1️⃣ | השוואה | `==` | Equal to | מחזיר true אם שני הערכים שווים | `5 == 5` | ✅ true |
| 1️⃣ | השוואה | `!=` | Not equal to | מחזיר true אם הערכים שונים | `5 != 3` | ✅ true |
| 2️⃣ | השוואה | `<` | Less than | בודק אם הערך הראשון קטן מהשני | `4 < 7` | ✅ true |
| 2️⃣ | השוואה | `>` | Greater than | בודק אם הערך הראשון גדול מהשני | `9 > 12` | ❌ false |
| 2️⃣ | השוואה | `<=` | Less or equal | קטן או שווה | `5 <= 5` | ✅ true |
| 2️⃣ | השוואה | `>=` | Greater or equal | גדול או שווה | `8 >= 6` | ✅ true |
| 3️⃣ | לוגי | `!` | NOT | הופך את הערך הבוליאני | `!true` | ❌ false |
| 4️⃣ | לוגי | `&&` | AND | true רק אם שני התנאים נכונים | `x > 0 && x < 10` | true אם x בין 1 ל־9 |
| 5️⃣ | לוגי | <code>&#124;&#124;</code> | OR | true אם לפחות אחד מהתנאים נכון |  <code>x &lt; 0 &#124;&#124; x &gt; 10</code> | true אם x מחוץ לטווח |

# תרגיל כיתה

פתח פרוייקט חדש וכתוב בו קוד עם שתי דוגמאות לשימוש בכל אחד מהאופרטורים הבאים:

- שימוש ב"גם" (AND): &&
- שימוש ב"או" (OR): || 
- שימוש באופרטור השלילה (NOT): !

בנוסף, כתוב דוגמא אחת המשלבת שני אופרטורים לפחות

בכל דוגמא עליך לקלוט את כל הנתונים הנדרשים מהמשתמש, הקלט יכול להיות טקסטואלי (מחרוזת) או מספרי (שלם או שבר, לפי הצורך) 

דוגמא לשימוש באופרטור "גם":

```csharp
Console.Write("Enter the temperature (°C): ");
float temperature = float.Parse(Console.ReadLine());

Console.Write("Is it sunny? (yes/no): ");
string sunnyInput = Console.ReadLine().ToLower();

if (temperature > 25 && sunnInput == "yes")
{
    Console.WriteLine("It's a good day for a swim!");
}
else
{
    Console.WriteLine("It's not a good day for a swim.");
}
```

