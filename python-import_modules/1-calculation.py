#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
suma = add(a, b)
print("{} + {} = {}".format(a, b, suma))
resta = sub(a, b)
print("{} - {} = {}".format(a, b, resta))
multi = mul(a, b)
print("{} * {} = {}".format(a, b, multi))
divi = div(a, b)
print("{} / {} = {}".format(a, b, divi))
