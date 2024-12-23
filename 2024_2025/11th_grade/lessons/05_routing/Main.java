public class Main {

    public static void main(String[] args) {
        var router = new Router();

        if (args.length > 0 && args[0].equals("all")) {
            System.out.println("Running all tests ");

            System.out.println("Testing HashRouter");
            var testRouter = new HashRouter();
            Tests.test(testRouter);

            System.out.println("Testing HashRouter2");
            var testRouter2 = new HashRouter2();
            Tests.test(testRouter2);
            return;
        }

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