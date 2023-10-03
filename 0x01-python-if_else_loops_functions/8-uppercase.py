#!/usr/bin/python3

def uppercase(str):
    """This function prints or converts a string in/to uppercase."""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
