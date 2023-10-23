#!/usr/bin/python3
# 1-safe_print_integer.py


ef safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
