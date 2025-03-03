import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;


class IteratorException extends Exception {
    // We don't need anything special here, just define a specific type of exception
    // so it will not be confused with other exceptions.
}

interface MyIterable {
    int getNext() throws IteratorException;
}

class MyIterableList implements MyIterable{

    // defining 'iterator' as 'final' makes it impossible to change it
    // after it was set in the constructor
    final private Iterator<Integer> iterator;
    MyIterableList(List<Integer> lst) {

        this.iterator = lst.iterator();
    }

    // using the @Override annotation is helping us to make sure that we
    // indeed override the interface method and didn't misspell it
    @Override
    public int getNext() throws IteratorException {
        if (!this.iterator.hasNext())
            throw new IteratorException();
        return this.iterator.next();
    }
}

class MyIterableRandom implements MyIterable{
    final private Random rnd;
    MyIterableRandom() {
        this.rnd = new Random();
    }

    @Override
    public int getNext() {
        return this.rnd.nextInt();
    }
}

class MyIterableFile implements MyIterable {

    final private Scanner scanner;
    MyIterableFile(String filePath) throws FileNotFoundException {

        this.scanner = new Scanner(new File(filePath));
    }

    @Override
    public int getNext() {
        return this.scanner.nextInt();
    }
}

public class Main {
    public static void main(String[] args) throws FileNotFoundException {

        var source1 = new MyIterableList(Arrays.asList(new Integer[]{1, 2, 3, 4, 5, 6}));
        var source2 = new MyIterableRandom();
        var source3 = new MyIterableFile("numbers.txt");

        // because all sources share the same interface, we can use an array
        // of MyIterable to hold all of them
        var sources = new MyIterable[]{ source1, source2, source3} ;
        while (true) {
            try {
                for (var source: sources) {
                    var item = source.getNext();
                    System.out.println(item);
                }
            } catch (IteratorException e){
                break;
            }
            // add a new line after each chuck of numbers from different sources
            System.out.println();
        }
    }
}