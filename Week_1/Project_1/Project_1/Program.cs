using System.Numerics;

public class Program
{
    public static void Main()
    {
        fact();
    }

    public static void fact()
    {
        BigInteger num = new BigInteger(); // At first, I was going to use int but unlike python ints in C# are bounded by their size, so I used BigInteger which is an object. I think python works similar to this under the hood but I am not sure.
        Console.WriteLine("Enter a positive Integer: ");
        string snum = Console.ReadLine();  
        num = BigInteger.Parse(snum);
        while (num < 0)
        {
            Console.WriteLine("Sorry, only pisitive numbers, enter again: ");
            snum = Console.ReadLine();
            num = BigInteger.Parse(snum);
        }
        if (num == 0)
        {
            Console.WriteLine("Factorial of 0 is 1");
        }
        else
        {
            BigInteger f = 1;
            for (BigInteger i = 1; i <= num; i++)
            {
                f = f * i;
            }
            Console.WriteLine("Factorial of " + num + " is " + f); // This is the line where I noticed a loss of precision due to an overflow of the C# integer value. 
        }
    }
}

// Brady Johnson
// IDE: Visual Studio 2022 
// Language version: .NET 8.0


