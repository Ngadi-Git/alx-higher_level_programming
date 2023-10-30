#!/usr/bin/python3
# 4-rectangle.py
# # Lennon N. Paul <ngadi.l.paul@gmail.com>
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle object"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle object"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * ((self.__width) + (self.__height)))

    def __str__(self):
        """Returns the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectObj = []
        for i in range(self.__height):
            [rectObj.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectObj.append("\n")
        return ("".join(rectObj))

    def __repr__(self):
        """Returns the string representation of the Rectangle object."""
        rectObj = "Rectangle(" + str(self.__width)
        rectObj += ", " + str(self.__height) + ")"
        return (rectObj)
