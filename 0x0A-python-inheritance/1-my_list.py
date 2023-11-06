#!/usr/bin/python3
# 1-my_list.py
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements a sorted print for the list class."""

    def print_sorted(self):
        """Prints a list in ascending order."""
        print(sorted(self))
