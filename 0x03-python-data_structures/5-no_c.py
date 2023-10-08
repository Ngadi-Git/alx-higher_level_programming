#!/usr/bin/python3

def no_c(my_string):
    newStr = ''
    for index in my_string:
        if index != 'c' and index != 'C':
            newStr += index
    return (newStr)
