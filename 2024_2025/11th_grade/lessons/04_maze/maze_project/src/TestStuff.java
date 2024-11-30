import java.util.LinkedList;
import java.util.List;

public class TestStuff {
    static List<Point> GoodSolution = List.of(new Point(0,0),
            new Point(0,1), new Point(0, 2), new Point(1, 2), new Point(2, 2),
            new Point(2, 3), new Point(2, 4), new Point(3,4), new Point(4, 4),
            new Point(5, 4), new Point(5, 5));

    // Same like before, just longer
    static List<Point> LongSolution = List.of(new Point(0,0),
            new Point(0,1), new Point(0, 2), new Point(1, 2), new Point(2, 2),
            new Point(2, 3), new Point(2, 4), new Point(3,4), new Point(4, 4),
            new Point(5, 4), new Point(5, 3), new Point(5,4), new Point(5, 5));

    // doesn't start on 0,0
    static List<Point> BadSolution1 = List.of(new Point(0,1),
            new Point(0,1), new Point(0, 2), new Point(1, 2), new Point(2, 2),
            new Point(2, 3), new Point(2, 4), new Point(3,4), new Point(4, 4),
            new Point(5, 4), new Point(5, 5));

    // doesn't end on 5,5
    static List<Point> BadSolution2 = List.of(new Point(0,0),
            new Point(0,1), new Point(0, 2), new Point(1, 2), new Point(2, 2),
            new Point(2, 3), new Point(2, 4), new Point(3,4), new Point(4, 4),
            new Point(5, 4), new Point(5, 3));

    // hits a wall
    static List<Point> BadSolution3 = List.of(new Point(0,0),
            new Point(0,1), new Point(1, 2), new Point(1, 2), new Point(2, 2),
            new Point(2, 3), new Point(2, 4), new Point(3,4), new Point(4, 4),
            new Point(5, 4), new Point(5, 5));

    // Disconnected
    static List<Point> BadSolution4 = List.of(new Point(0,0),
            new Point(0, 2), new Point(1, 2), new Point(2, 2),
            new Point(2, 3), new Point(2, 4), new Point(3,4), new Point(4, 4),
            new Point(5, 4), new Point(5, 5));

    // Moves diagonally
    static List<Point> BadSolution5 = List.of(new Point(0,0),
            new Point(0,1), new Point(0, 2), new Point(1, 2), new Point(2, 2),
            new Point(2, 3), new Point(2, 4), new Point(3,4), new Point(4, 4),
            new Point(5, 5));



}
