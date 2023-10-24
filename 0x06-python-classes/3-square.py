#!/usr/bin/python3
# 3-square.py
"""Defining a class Square."""


class Square:
    """Creates a new square class."""

    def __init__(self, size=0):
        """Initialize a new square instance.

        Args:
            size (int): The size of the new square instance.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square object."""
        return (self.__size * self.__size)
