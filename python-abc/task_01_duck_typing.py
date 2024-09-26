#!/usr/bin/env python3
"""
Shapes, Interfaces, and Duck Typing
"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract class Shape with two
    abstract methods: area and perimeter
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Circle class inherits from Shape
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2*(pi * self.radius)


class Rectangle(Shape):
    """
    Rectangle class inherits from Shape
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape.
    """

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
