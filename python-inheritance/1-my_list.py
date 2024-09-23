#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """
    class MyList inherits from list

    Methods:
        print_sorted(self): Prints list in ascending order.
    """
    def print_sorted(self):
        """
        Prints list, but sorted (ascending sort)
        """
        print(sorted(self))
