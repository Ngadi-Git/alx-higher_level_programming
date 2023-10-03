#!/usr/bin/python3
# Author - Lennon PAUL

for base in range(0, 10):
    for second in range(base + 1, 10):
        if base == 8 and second == 9:
            print("{}{}".format(base, second))
        else:
            print("{}{}".format(base, second), end=", ")
