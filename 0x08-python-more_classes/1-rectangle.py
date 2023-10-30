#!/usr/bin/python3
# 1-rectangle.py
# Lennon N. Paul <ngadi.l.paul@gmail.com>
"""Defines a rectangle class."""

class Rectangle:
    """Represents a rectangle."""


    def __init__(self, width, height):
        """Initializes a new Rectangle instance.

        Args:
            width(int): The width of the new Rectangle instance.
            height(int): The height of the new Rectangle instance.
        """

        self.width = width
        self.height = height

    @property 
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self, value):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle instance."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    
