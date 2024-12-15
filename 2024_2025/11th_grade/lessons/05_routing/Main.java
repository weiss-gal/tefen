class Router {
    // for example 101 -> "A", 102 -> "Tel Aviv"
    void addRoute(int address, String target) {

    }

    String resolveRoute(int address) {
        return "Tel Aviv ";
    }
}


public class Main {
    public static void main(String[] args) {
        var router = new Router();

        router.addRoute(1, "Tel Aviv");
        router.addRoute(2, "Beer Sheva");
        router.addRoute(3, "Haifa");

        // test 1
        var result1 = router.resolveRoute(1);
        System.out.println("The route for address 1 is: " + result1);
        System.out.println("Test 1: " + (result1.equals("Tel Aviv") ? "Pass" : "Fail"));

        // test 2
        var result2 = router.resolveRoute(2);
        System.out.println("The route for address 2 is: " + result2);
        System.out.println("Test 2: " + (result1.equals("Beer Sheva") ? "Pass" : "Fail"));
    }
}