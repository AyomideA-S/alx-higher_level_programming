#!/usr/bin/python3
import hidden_4


def principal():
    for i in dir(hidden_4):
        if i[0] != '_' or i[1] != '_':
            print(i)


if __name__ == "__main__":
    principal()
