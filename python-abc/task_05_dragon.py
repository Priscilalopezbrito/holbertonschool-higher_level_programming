#!/usr/bin/env python3
"""
The Mystical Dragon - Mastering Mixins
"""


class SwimMixin:
    """
    Creating Mixins
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Creating Mixins
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Implementing Dragon
    """
    def roar(self):
        print("The dragon roars!")
