#!/usr/bin/python3
# 1-safe_print_integer.py

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        return False
    else:
        return True
