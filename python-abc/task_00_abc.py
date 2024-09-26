#!/usr/bin/env python3
"""
Abstract Animal Class and its Subclasses
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Class Animal
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Subclass Dog
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Subclass Cat
    """

    def sound(self):
        return "Meow"
