# משתנים פרימיטיביים

משתנים פרימיטיביים משמשים לאחסון מידע כגון ערכים מספריים ובוליאניים. הם **אינם** אובייקטים ולכן אין להם פעולות משל עצמם. 

כדי לראות כמה סוגים ננסה להריץ את הקוד הבא:
```
import static java.lang.System.out;

public class Main {
    public static void main(String[] args) {
        out.print("1 => ");
        out.println(1);

        out.print("1 + 1 => ");
        out.println(1 + 1);

        out.print("10 / 2 => ");
        out.println(10 / 2);

        out.print("1 / 2 => ");
        out.println(1 / 2);

        // Integer numbers vs Floating point
        out.print("1.0 / 2 => ");
        out.println(1.0 / 2);

        out.print("1 / 2.0 => ");
        out.println(1 / 2.0);

        out.print("1.0 + 1.0=> ");
        out.println(1.0 + 1.0);

        // Booleans
        out.print("true=> ");
        out.println(true);

        out.print("1 == 1=> ");
        out.println(1 == 1);

        out.print("1 == 2=> ");
        out.println(1 == 2);

        out.print("1 == 1.0=> ");
        out.println(1 == 1.0);

        // Why we don't ever want to check equality of floating point
        out.print("1.0/3.0=> ");
        out.println(1.0/3.0);

        out.print("0.3333333333333333 == 1/3=> ");
        out.println(0.3333333333333333 == 1/3);
    }
}
```
