#!/usr/bin/python3
# 100-safe_print_integer_err.py

import sys


def safe_print_integer_err(value):
try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as e:
        sys.stderr.write("Exception: {}\n".format(e.args[0]))
        return (False)
