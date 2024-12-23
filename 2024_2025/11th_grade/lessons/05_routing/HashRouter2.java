import java.util.LinkedList;



/**
 * The HashRouter2 class extends the Router class and provides a hash-based routing mechanism.
 * It uses binary modulu to hash the address and store the routes in a linked list.
 */
public class HashRouter2 extends Router {
    private final LinkedList<Pair>[] routes;

    public HashRouter2() {
        routes = (LinkedList<Pair>[]) new LinkedList[1024];
    }

    private int hash(int address) {
        return address & 0x3FF;
    }

    @Override
    void addRoute(int address, String target) {
        var index = hash(address);
        if (routes[index] == null) {
            routes[index] = new LinkedList<>();
        }
        routes[index].add(new Pair(address, target));
    }

    @Override
    String resolveRoute(int address) {
        var index = hash(address);
        if (routes[index] == null) {
            return null;
        }
        for (var pair : routes[index]) {
            if (pair.address == address) {
                return pair.target;
            }
        }
        return null;

    }

    @Override
    public void clean() {
        for (int i = 0; i < routes.length; i++) {
            routes[i] = null;
        }
    }
}
