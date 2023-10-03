#!/usr/bin/python3

def fizzbuzz():
    """Prints the numbers from 1 to 100 separated by a space.

    For multiples of three, print Fizz.
    For multiples of five, print Buzz.
    For multiples of three and five, print FizzBuzz.
    """
    for dig in range(1, 101):
        if dig % 3 == 0 and dig % 5 == 0:
            print("FizzBuzz ", end="")
        elif dig % 3 == 0:
            print("Fizz ", end="")
        elif dig % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(dig), end="")
