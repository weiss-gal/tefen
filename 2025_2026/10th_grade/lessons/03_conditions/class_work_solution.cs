
class Program
{
    static void Main()
    {
        // Step 1: Get name
        Console.Write("What is your name? ");
        string name = Console.ReadLine();
        Console.WriteLine("Hello " + name);

        // Step 2: Get age
        Console.Write("How old are you? ");
        int age = int.Parse(Console.ReadLine());
        Console.WriteLine("You are " + age + " years old");

        // Step 4: Get height
        Console.Write("How tall are you (in cm)? ");
        int height = int.Parse(Console.ReadLine());

        // Step 3–6: Apply conditions
        if (age >= 12)
        {
            if (height >= 140)
            {
                Console.WriteLine("You can ride the rollercoaster!");
            }
            else
            {
                Console.WriteLine("Sorry, you are not tall enough.");
            }
        }
        else
        {
            if (height >= 160)
            {
                Console.WriteLine("You are unusually tall — you can ride!");
            }
            else if (age >= 10)
            {
                Console.Write("Do you have parental permission (yes/no)? ");
                string permission = Console.ReadLine().ToLower();

                if (permission == "yes")
                {
                    Console.WriteLine("Great, with permission you can ride!");
                }
                else
                {
                    Console.WriteLine("Sorry, without permission you cannot ride.");
                }
            }
            else
            {
                Console.WriteLine("Sorry, you are too young and not tall enough.");
            }
        }
    }
}
