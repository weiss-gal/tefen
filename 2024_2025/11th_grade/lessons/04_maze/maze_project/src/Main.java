
import java.util.LinkedList;
import java.util.List;

class MyMaze extends Maze{
    private int[][] content = new int[][] {
            new int [] {0,1,0,1,0,1},
            new int [] {0,1,0,1,0,1},
            new int [] {0,0,0,1,0,0},
            new int [] {1,1,0,1,1,0},
            new int [] {0,0,0,0,0,0},
            new int [] {1,0,1,1,1,0},
    };

    @Override
    public int getHeight() {
        return content.length;
    }

    @Override
    public int getWidth() {
        return content[0].length;
    }

    @Override
    public boolean hasWall(int x, int y) {
        return false;
    }
}



public class Main {
    static LinkedList<Point> solution = new LinkedList<>();

    static boolean checkSolution(Maze maze, List<Point> solution) {
        return false;
    }

    public static void main(String[] args) {
        solution.add(new Point(0,0));
        solution.add(new Point(0, 1));
        solution.add(new Point(0, 2));
        solution.add(new Point(1, 2));
        solution.add(new Point(2, 2));
        solution.add(new Point(2, 3));
        solution.add(new Point(2, 4));
        solution.add(new Point(3, 4));
        solution.add(new Point(4, 4));
        solution.add(new Point(5, 4));
        solution.add(new Point(5, 5));

        var myMaze = new MyMaze();

        var s = solution;
        var result = checkSolution(myMaze, s);
        System.out.println("The Solution is:" + s);
        System.out.println("The Solution " + (result ? "Solve" : "does not solve") + " the maze");
    }
}