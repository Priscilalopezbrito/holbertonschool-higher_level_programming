#!/usr/bin/python3
import sys

if __name__ == "__main__":
    add = 0
    count = len(sys.argv)
    if count < 2:
        print("0")
    else:
        for args in sys.argv[1:]:
            add += int(args)
        print(add)
