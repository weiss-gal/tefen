import java.nio.file.Path;
import java.nio.file.Files;

class Main {
    public static void main(String[] args) throws Exception {
        // read a file
        Path filePath = Path.of("input.txt");
        
        var lines = Files.readAllLines(filePath);
        lines.forEach(System.out::println);
    }
}
