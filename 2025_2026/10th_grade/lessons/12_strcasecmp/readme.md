# תרגיל - מימוש הפונקציה strcasecmp

יש לממש את הפונקציה strcasecmp באמצעות השוואת תווים בלבד, ללא פונקציות עזר כגון ToLower(). 
לחלופין, אם אתם רוצים להשתמש בפונקציות עזר כגון ToLower() יש לממש אותן בעצמכם



```csharp
using System;

public static class Program
{
    /// <summary>
    /// Exercise: Implement a C-like strcasecmp (case-insensitive string compare).
    ///
    /// Contract:
    /// - Return 0 if the strings are equal ignoring case.
    /// - Return < 0 if s1 < s2 (lexicographically, ignoring case).
    /// - Return > 0 if s1 > s2 (lexicographically, ignoring case).
    ///
    /// TODO: Replace this stub with a real implementation.
    /// </summary>
    public static int StrCaseCmp(string s1, string s2)
    {
        // STUB for students
        return 0;
    }

    public static void Main()
    {
        int passed = 0;
        int total = 0;

        WriteHeader("Running StrCaseCmp tests");

        // 1) Equal (same case)
        {
            total++;
            int result = StrCaseCmp("hello", "hello");
            if (PrintResult("Equal (same case)", "hello", "hello", result, expectedSign: 0)) passed++;
        }

        // 2) Equal (different case)
        {
            total++;
            int result = StrCaseCmp("Hello", "hELLo");
            if (PrintResult("Equal (different case)", "Hello", "hELLo", result, expectedSign: 0)) passed++;
        }

        // 3) Less-than by letter
        {
            total++;
            int result = StrCaseCmp("abc", "abd");
            if (PrintResult("Less-than by letter", "abc", "abd", result, expectedSign: -1)) passed++;
        }

        // 4) Greater-than by letter
        {
            total++;
            int result = StrCaseCmp("abe", "abd");
            if (PrintResult("Greater-than by letter", "abe", "abd", result, expectedSign: +1)) passed++;
        }

        // 5) Prefix shorter is less
        {
            total++;
            int result = StrCaseCmp("abc", "abcd");
            if (PrintResult("Prefix shorter is less", "abc", "abcd", result, expectedSign: -1)) passed++;
        }

        // 6) Prefix longer is greater
        {
            total++;
            int result = StrCaseCmp("abcd", "abc");
            if (PrintResult("Prefix longer is greater", "abcd", "abc", result, expectedSign: +1)) passed++;
        }

        // 7) Empty vs non-empty (empty is less)
        {
            total++;
            int result = StrCaseCmp("", "a");
            if (PrintResult("Empty vs non-empty", "", "a", result, expectedSign: -1)) passed++;
        }

        // 8) Non-empty vs empty (non-empty is greater)
        {
            total++;
            int result = StrCaseCmp("a", "");
            if (PrintResult("Non-empty vs empty", "a", "", result, expectedSign: +1)) passed++;
        }

        // 9) Equal empty strings
        {
            total++;
            int result = StrCaseCmp("", "");
            if (PrintResult("Empty equals empty", "", "", result, expectedSign: 0)) passed++;
        }

        Console.WriteLine();
        WriteSummary(passed, total);
    }

    /// <summary>
    /// Prints a single test result with color and returns true/false for pass/fail.
    /// expectedSign: 0 (equal), -1 (result should be < 0), +1 (result should be > 0)
    /// </summary>
    private static bool PrintResult(string name, string a, string b, int result, int expectedSign)
    {
        int sign = Math.Sign(result);
        bool ok = sign == expectedSign;

        WriteStatus(ok ? "PASS" : "FAIL", ok);
        Console.WriteLine($" {name}");

        WriteDim("   A: "); WriteValue(a);
        WriteDim("   B: "); WriteValue(b);

        WriteDim("   Result: "); WriteNumber(result);
        WriteDim("   Expected sign: "); WriteNumber(expectedSign);

        Console.WriteLine();
        return ok;
    }

    // ---------- Coloring helpers ----------

    private static void WriteHeader(string text)
    {
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine(text);
        Console.WriteLine(new string('=', text.Length));
        Console.ResetColor();
        Console.WriteLine();
    }

    private static void WriteStatus(string text, bool success)
    {
        Console.ForegroundColor = success ? ConsoleColor.Green : ConsoleColor.Red;
        Console.Write($"[{text}]");
        Console.ResetColor();
    }

    private static void WriteSummary(int passed, int total)
    {
        Console.ForegroundColor = passed == total ? ConsoleColor.Green : ConsoleColor.Yellow;
        Console.WriteLine($"Summary: {passed}/{total} tests passed");
        Console.ResetColor();
    }

    private static void WriteDim(string text)
    {
        Console.ForegroundColor = ConsoleColor.DarkGray;
        Console.WriteLine(text);
        Console.ResetColor();
    }

    private static void WriteValue(string s)
    {
        Console.ForegroundColor = ConsoleColor.White;
        Console.WriteLine($"      \"{s}\"");
        Console.ResetColor();
    }

    private static void WriteNumber(int n)
    {
        Console.ForegroundColor =
            n == 0 ? ConsoleColor.White :
            n < 0 ? ConsoleColor.Yellow :
                    ConsoleColor.Cyan;

        Console.WriteLine($"      {n}");
        Console.ResetColor();
    }
}

```