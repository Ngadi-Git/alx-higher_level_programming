#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(a, b):
    result = 0
    for index in range(1, 3):
        try:
            if index > a:
                raise Exception('Too far')
            else:
                result += a ** b / index
        except:
            result = b + a
            break
    return (result)
