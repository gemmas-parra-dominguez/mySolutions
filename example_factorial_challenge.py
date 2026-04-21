""" Factorial Challenge

The factorial function gives the number of possible arrangements of a set of items of length "n"
For example, there are 4! ("four factorial") or 24 ways to arrange four items, which can be calculated as: 
4 * 3 * 2 * 1
5! = 5 * 4 * 3 * 2 * 1 = 120
6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
etc.

In a set of 0 items (an empty set) there is only one way to arrange the items, therefore, 0! = 1
For the purposes of this exercise, factorials are only defined for **positive integers** (including 0) """

def get_factorial(input):
    if type(input) != int:
        print(f"Input is of type {type(input)}, input is converted to integer!")
    num = int(input)

    if (num < 0):
        print("Only positive integers allowed!")
        return -1

    if (num == 0):
        return 1
    return num * get_factorial(num - 1)

print("factorial of 4 is", get_factorial(4))
print("factorial of 5 is", get_factorial(5))
print("factorial of 6 is", get_factorial(6))
print("factorial of '7' is", get_factorial('7'))
print("factorial of 8.2 is", get_factorial(8.2))
print("factorial of -1.2 is", get_factorial(-1.2))
