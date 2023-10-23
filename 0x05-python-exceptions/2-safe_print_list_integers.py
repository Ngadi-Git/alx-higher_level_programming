#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    tot = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            tot += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (tot)
