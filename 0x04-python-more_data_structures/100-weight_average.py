#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        digit = 0
        bottom = 0
        for top in my_list:
            digit += (top[0] * top[1])
             += (top[1])
        return (digit/bottom)
    return 0
