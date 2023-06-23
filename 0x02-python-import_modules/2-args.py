#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    ac = len(argv) - 1

    if ac == 0:
        print(f'{ac} arguments.')
    else:
        if ac == 1:
            print(f'{ac} argument:')
        else:
            print(f'{ac} arguments:')
        for i in range(1, ac + 1):
            print(f'{i}: {argv[i]}')
