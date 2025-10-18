// שלב 2 — קבלת בחירות מהשחקנים

// בקשת בחירה מהשחקן הראשון
Console.Write("Type player 1 move (1-rock, 2-paper, 3-scissors): ");
int player1 = int.Parse(Console.ReadLine());

// הדפסת בחירת השחקן הראשון
Console.WriteLine("Player 1 chose " + player1);

// בקשת בחירה מהשחקן השני
Console.Write("Type player 2 move (1-rock, 2-paper, 3-scissors): ");
int player2 = int.Parse(Console.ReadLine());

// הדפסת בחירת השחקן השני
Console.WriteLine("Player 2 chose " + player2);
