using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

public struct Token
{
    public string data;
    public int recipient;
    public Token(string p1, int p2)
    {
        data = p1;
        recipient = p2;
    }
}
namespace ConsoleApplication3
{
    class Program
    {
        static void Main(string[] args)
        {
            Token token = new Token("data", 10);
            Thread thread = new Thread(() => ThreadFunction(1, token));
            thread.Start();
        }
        static void ThreadFunction(int i, Token t)
        {
            if (t.recipient == i)
            {
                Console.WriteLine("data:" + t.data + " recipient:" + i);
            }
            else
            {
                Thread thread = new Thread(() => ThreadFunction(i + 1, t));
                thread.Start();
            }
        }
    }
}
