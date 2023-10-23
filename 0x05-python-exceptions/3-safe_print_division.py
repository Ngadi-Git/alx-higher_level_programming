#!/usr/bin/python3
# 3-safe_print_division.py

def safe_print_division(a, b):
    try:
        quotnt = a / b
    except (TypeError, ZeroDivisionError):
        quotnt = None
    finally:
        print("Inside result: {}".format(quotnt))
    return (quotnt)
