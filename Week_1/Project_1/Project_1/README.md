Date: 10/10/2021 <br />
Name: Brady Johnson <br />
IDE: Visual Studio 2022 <br />
Language version: .NET 8.0 <br />

Translating the following code from Python to C#:
```python

def fact():
    n = int(input("Enter a positive Integer: "))
    while((n < 0)):
        n =int(input("Sorry, only positive numbers, enter again: "))
    if (n == 0):
        print("The factorial of 0 is 1")
    else:
        f = 1
        for i in range(1, n+1):
            f = f * i
        print("The factorial of", n, "is", f)

fact()

```


* The only trick that was almost missed was the need to use BigInteger to handle large numbers. I had almost forgotten that C# does not automatically handle large numbers like Python does.
