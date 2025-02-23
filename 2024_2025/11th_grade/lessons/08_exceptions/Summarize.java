import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import static java.lang.System.out;

public class Summarize {
    public static void main(String[] args) throws Exception {
        final String Filename = "data.txt";
        final File file = new File(Filename);

        var reader = new BufferedReader(new FileReader(file));
        // iterate over the file line by line
        String line;
        int sum = 0;
        while ((line = reader.readLine()) != null) {
            sum += Integer.parseInt(line);
        }

        out.println("Sum: " + sum);
     
    }
}