// שלב 3 — הצגת הבחירות בצורה קריאה

// בקשת בחירה מהשחקן הראשון
Console.Write("Type player 1 move (1-rock, 2-paper, 3-scissors): ");
int player1 = int.Parse(Console.ReadLine());

// בקשת בחירה מהשחקן השני
Console.Write("Type player 2 move (1-rock, 2-paper, 3-scissors): ");
int player2 = int.Parse(Console.ReadLine());

// הצגת הבחירה של כל שחקן באנגלית לפי המספר
if (player1 == 1)
{
    Console.WriteLine("Player 1 chose rock.");
}
else if (player1 == 2)
{
    Console.WriteLine("Player 1 chose paper.");
}
else if (player1 == 3)
{
    Console.WriteLine("Player 1 chose scissors.");
}

if (player2 == 1)
{
    Console.WriteLine("Player 2 chose rock.");
}
else if (player2 == 2)
{
    Console.WriteLine("Player 2 chose paper.");
}
else if (player2 == 3)
{
    Console.WriteLine("Player 2 chose scissors.");
}
