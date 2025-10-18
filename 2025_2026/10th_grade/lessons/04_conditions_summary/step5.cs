// שלב 4 — קביעת התוצאה

// בקשת הבחירות משני השחקנים
Console.Write("Type player 1 move (1-rock, 2-paper, 3-scissors): ");
int player1 = int.Parse(Console.ReadLine());

Console.Write("Type player 2 move (1-rock, 2-paper, 3-scissors): ");
int player2 = int.Parse(Console.ReadLine());

// הצגת הבחירות
if (player1 == 1)
    Console.WriteLine("Player 1 chose rock.");
else if (player1 == 2)
    Console.WriteLine("Player 1 chose paper.");
else if (player1 == 3)
    Console.WriteLine("Player 1 chose scissors.");

if (player2 == 1)
    Console.WriteLine("Player 2 chose rock.");
else if (player2 == 2)
    Console.WriteLine("Player 2 chose paper.");
else if (player2 == 3)
    Console.WriteLine("Player 2 chose scissors.");

// קביעת התוצאה
if (player1 == player2)
{
    Console.WriteLine("Result: It's a draw!");
}
else if ((player1 == 1 && player2 == 3) ||
         (player1 == 2 && player2 == 1) ||
         (player1 == 3 && player2 == 2))
{
    Console.WriteLine("Result: Player 1 wins!");
}
else
{
    Console.WriteLine("Result: Player 2 wins!");
}
