#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = (tuple_a + (0, 0))[:2]
    tuple_b = (tuple_b + (0, 0))[:2]
    suma = zip(tuple_a, tuple_b)
    result = tuple(map(sum, suma))
    return result
