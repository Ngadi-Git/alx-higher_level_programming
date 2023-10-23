#!/usr/bin/python3

def safe_print_liist(my_list=[], x=0):
    total = 0
    for index in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            total += 1
        except IndexError:
            break
    print("")
    return (total)
