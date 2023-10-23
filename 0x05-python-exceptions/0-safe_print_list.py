#!/usr/bin/python3

def safe_print_liist(my_list=[], x=0):
    total = 0
    for index in range(0, x):
        try:
            print(my_list[index], end='')
            total += 1
        except IndexError:
            break
    print('')
    return (total)
