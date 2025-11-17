# תיאור מספר

הקוד הבא מקבל מספר מהמשתמש ומנסח אותו בתור פעולת כפל יחד עם חיבור , למשל אם ניתן לו את המספר 7 הוא יכול לתאר אותו בתור פעמיים 3 ועוד 1 או פעם אחת 4 ועוד 3. 
המחלק (3 או 4 בדוגמא) נקבע באופן אקראי. 
עם זאת, מדי פעם הקוד נתקע באמצע הריצה ומוציא הודעת שגיאה. 
בצע מספר הרצות ככל שתרצה ושים לב לבעיה שמתרחשת מדי פעם. 
כאשר היא מתרחשת, השתמש בכדי הדיבאג כדי למצוא אותה. 

```csharp
Console.Write("Enter a number: ");
int target = int.Parse(Console.ReadLine());

Random rnd = new Random();

int factor = rnd.Next(0, 5); // sometimes 0 → crash
int quotient = target / factor; // DivideByZeroException
int remainder = target % factor;

Console.WriteLine($"{target} can be created by {quotient} times {factor} plus {remainder}");
```