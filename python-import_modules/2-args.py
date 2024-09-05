#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    count = len(sys.argv)
    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("{} argument:".format(count - 1))
    else:
        print("{} arguments:".format(count - 1))
    i = 1
    for args in argv:
        print("{}: {}".format(i, args))
        i = i + 1
