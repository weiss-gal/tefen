import java.util.Scanner;

public class BuggySolution1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int secretNumber = 7;  // The number the user needs to guess
        int userGuess = 0;     // Variable to store user's guess

        System.out.println("Guess the number between 1 and 10!");

        // While loop to keep asking the user for a guess until they get it right
        while (userGuess == secretNumber) {
            System.out.print("Enter your guess: ");
            userGuess = scanner.nextInt();  // Read the user's input

            // Use an if-else to give feedback based on the guess
            if (userGuess > secretNumber) {
                System.out.println("Too low! Try again.");
            } else if (userGuess < secretNumber) {
                System.out.println("Too high! Try again.");
            } else {
                System.out.println("Congratulations! You've guessed the right number.");
            }
        }

        scanner.close();
    }
}
