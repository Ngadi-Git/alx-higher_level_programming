#!/usr/bin/python3

def uniq_add(my_list=[]):
    digit = 0
    for value in set(my_list):
        digit += value
    return (digit)
