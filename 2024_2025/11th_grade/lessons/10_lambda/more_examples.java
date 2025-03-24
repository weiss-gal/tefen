
// NOTE: a 'record' is a new feature in Java 16. 
// It is a class that is used to store data. 
// It is similar to a class, but it is more concise. It is immutable, which means that once you create a record object, 
// you cannot change its values. You can only read them.

import java.util.Arrays;
import java.util.List;

record person(String firstName, String lastName, int age) {}

class Main {

    private static void PrettyPrint(person p) {
        System.out.println(p.firstName() + " " + p.lastName() + "[" + p.age() + "]");
    }
     
    public static void main(String[] args) {
        person[] people = {
            new person("John", "Doe", 30),
            new person("Jane", "Smith", 25),
            new person("Emily", "Jones", 40)
        };

        
        // we can sort it by name
        var sorted = Arrays.stream(people).sorted((p1, p2) -> {
            var cmp = p1.lastName().compareTo(p2.lastName());
            if (cmp == 0) {
                return p1.firstName().compareTo(p2.firstName());
            }
            return cmp;
        });

        // and then print it
        sorted.forEach(p -> PrettyPrint(p));

        // or we can chain several operators
        var count = Arrays.stream(people)
            .filter(p -> p.age() > 30)
            .count();

        System.out.println("People older than 30: " + count);

        // we can also use a list, which converts very well to stream 
        var list = List.of(
            new person("john", "doe", 30),
            new person("jane", "smith", 25),
            new person("emily", "jones", 40)
        );

        // convert names to uppercase
        list.stream()
            .map(p -> new person(p.firstName().toUpperCase(), p.lastName().toUpperCase(), p.age()))
            .forEach(p -> PrettyPrint(p));
            
        // more stream actions here:
        // https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html
    }
    
}
