namespace Hello2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string name;
            // Writing directions to the user
            Console.WriteLine("Hello, What is your name?");

            // Reading the user input
            name = Console.ReadLine();

            // Greeting the user
            Console.WriteLine("Hello, " + name + ". Welcome to C# programming!");
        }
    }
}