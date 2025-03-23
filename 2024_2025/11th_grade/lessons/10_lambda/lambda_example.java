// דמות
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

interface MyPredicate<T>  {
    boolean isIncluded(T i);
}

public class Main {
    static void PrintAll(Character[] characters) {
        for (var c: characters) {
            System.out.println(c.toString());
        }
    }

    static <T> void PrintAll(T[] characters, MyPredicate<T> filter) {
        for (var c: characters) {
            if (filter.isIncluded(c))
                System.out.println(c.toString());
        }
    }

    public static void main(String[] args) {
        var myArr = new Character[] {
           new Character("timothy", 30),
           new Character("alexander", 32),
           new Character("shmebulock", 35)
        };

        //1
        System.out.println("Print all chars that start with a");

        PrintAll(myArr, (Character c) -> c.name.charAt(0) == 'a');

        //2
        System.out.println("Print all chars that are older than 32 (not including)");
        PrintAll(myArr, (Character c) -> {
            System.out.println("I am checking " + c.toString());
            return c.age > 32;
        });
    }
}
