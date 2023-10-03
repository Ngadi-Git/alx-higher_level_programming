#!/usr/bin/python3
# Author - Lennon PAUL

def islower(char):
    """The function checks for lowercase letters."""
    if ord(char) >= 97 and ord(char) <= 122:
        return True
    else:
        return False
