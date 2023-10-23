#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    tot = 0
    
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            tot += 1
        except IndexError:
            break
    print("")
    return (tot)
