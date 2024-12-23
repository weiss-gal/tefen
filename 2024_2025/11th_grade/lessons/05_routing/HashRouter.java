import java.util.LinkedList;

public class HashRouter extends Router {
    private final LinkedList<Pair>[] routes;

    public HashRouter() {
        routes = (LinkedList<Pair>[]) new LinkedList[1000];
    }

    private int hash(int address) {
        return address % 1000;
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
