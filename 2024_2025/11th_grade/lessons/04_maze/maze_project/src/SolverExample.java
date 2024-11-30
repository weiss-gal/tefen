import java.util.List;

public class SolverExample {
    static boolean checkSolution(Maze maze, List<Point> solution){
        // check start
        var first = solution.getFirst();
        if (first.x != 0 || first.y != 0)
            return false;
        var last =solution.getLast();
        if (last.x != maze.getWidth() -1 || last.y != maze.getHeight()-1)
            return false;

        Point prev = null;
        for (var curr: solution){
            if (prev != null) {
                double distance = Math.sqrt(Math.pow(prev.x - curr.x, 2) + Math.pow(prev.y - curr.y, 2));
                if (distance > 1)
                    return false;
            }
            prev = curr;
        }

        return true;
    }
}
