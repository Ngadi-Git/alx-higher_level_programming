#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count_total = 0
    for i in range(0, x):
        try:
            print(my_list[index], end='')
            count_total += 1
        except IndexError:
            break
    print('')
    return (count_total)
