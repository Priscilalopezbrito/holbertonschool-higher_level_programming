#!/usr/bin/python3
def uppercase(str):
    upp_str = ""
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            upp_str = upp_str + chr(ord(c) - 32)
        else:
            upp_str = upp_str + c
    print("{}".format(upp_str))
