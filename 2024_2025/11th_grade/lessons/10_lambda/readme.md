# פונקציות כאובייקט בJAVA (למבדא \ Lambda)

כפי שראינו, ניתן להשתמש בפונקצייה כאובייקט בשפת Java. במקרה כזה המחלקה של האובייקט יורשת ממשק (interface) מסוג מיוחד.
הממשק המשמש אותנו להעביר פונקציה הוא ממשק בו מוגדרת מתודה יחידה. למשל הממשק שישמש אותנו לצורך סינון אובייקטים מרשימה יהיה בעל מתודה יחידה שמקבלת אובייקט ומחזירה ערך בוליאני. 
דוגמא, נגדיר מחלקה כלשהיא:

```java
class Character {
    public String name;
    public int age;

    Character(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return name + " [" + age + "]";
    }
}
```

ולמחלקה הזו נגדיר ממשק עבור סינון:

```java
interface MyPredicate<Character>  {
    boolean isIncluded(Character c);
}
```

וכעת נוכל להשתמש בממשק הזה בקוד שלנו:

```java
 static void PrintAll(Character[] characters, MyPredicate filter) {
        for (var c: characters) {
            if (filter.isIncluded(c))
                System.out.println(c.toString());
        }
    }
```

כשנרצה להשתמש בפונקציה PrintAll נוכל להעביר מימוש של הממשק הזה בתור פרמטר, באופן הבא:
```java
//Print every character that is 30 years old or more
Printall(characters, (Character c) -> c.age >= 30);
```


## תרגיל סיכום
בקובץ read_file.java תוכלו למצוא דוגמת קוד לקריאת קובץ כstream. 

בעזרת הקוד הזה ופעולות stream בצעו את סט הפעולות הבא:

- המירו את הקובץ לstream של שורות
- השמט שורות ריקות
- מיינו לפי המספר בתחילת כל שורה
- השמיטו את שלושת השורות הראשונות
- השמיטו את חמשת השורות האחרונות
- השאירו רק את השורות שמתחלקות ב3 או 7
- הפכו רק את המילים
