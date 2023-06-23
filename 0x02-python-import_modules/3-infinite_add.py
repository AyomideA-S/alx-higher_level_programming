#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    res = sum(int(argv[cnt]) for cnt in range(1, len(argv)))
    print(res)
