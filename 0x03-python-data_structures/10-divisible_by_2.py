#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    multiplesOfTwo = []
    for index in range(len(my_list)):
        if my_list[index] % 2 == 0:
            multiplesOfTwo.append(True)
        else:
            multiplesOfTwo.append(False)

    return (multiplesOfTwo)
