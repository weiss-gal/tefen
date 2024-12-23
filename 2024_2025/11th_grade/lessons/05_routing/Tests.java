public class Tests {
    static void test(Router r){
        // basic test
        r.addRoute(1, "Tel Aviv");
        r.addRoute(2, "Beer Sheva");
        r.addRoute(3, "Haifa");

        var res = r.resolveRoute(1);
        System.out.println("Test 1: " + (res.equals("Tel Aviv") ? "Pass" : "Fail"));

        // Hash conflict test
        r.clean();
        for (int i = 0; i < 10000; i++) {
            r.addRoute(i, "Route " + i);
        }
        boolean pass = true;
        for (int i = 0; i < 10000; i++) {
            res = r.resolveRoute(i);
            if (!res.equals("Route " + i)) {
                pass = false;
                break;
            }
        }
        System.out.println("Test 2: " + (pass ? "Pass" : "Fail"));

        // Missing Route test
        r.clean();
        r.addRoute(1, "Tel Aviv");
        r.addRoute(2, "Beer Sheva");
        r.addRoute(3, "Haifa");
        res = r.resolveRoute(4);
        System.out.println("Test 3: " + (res == null ? "Pass" : "Fail"));

        // performance test
        r.clean();
        for (int i = 0; i < 1000; i++) {
            r.addRoute(i, "Route " + i);
        }
        pass = true;
        long start = System.currentTimeMillis();
        for (int i = 0; i < 1000000000; i++) {
            res = r.resolveRoute(1);
            if (!res.equals("Route 1")) {
                pass = false;
                break;
            }
        }
        long end = System.currentTimeMillis();

        System.out.println("Test 4: " + (pass ? "Pass" : "Fail"));
        System.out.println("Performance test: " + (end - start) + "ms");

    }

}
