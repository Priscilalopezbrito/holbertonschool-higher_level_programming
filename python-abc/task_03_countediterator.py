#!/usr/bin/env python3
"""
CountedIterator - Keeping Track of Iteration
"""


class CountedIterator:
    """
    CountedIterator extends the built-in iterator
    obtained from the iter function.
    """

    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.counter = 0

    def __next__(self):
        item = next(self.iterable)
        self.counter += 1
        return item

    def get_count(self):
        return self.counter
