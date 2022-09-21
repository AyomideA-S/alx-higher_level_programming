#!/usr/bin/python3

# print_last_digit: Function that print last digit of any number
# Number: Arguments that hold pass variable or value
# last: Holds last digit of passed argument
# Return: Last digit

def print_last_digit(number):
    if number < 0:
        last = (-1 * number) % 10

    else:
        last = number % 10

    print('{}'.format(last), end='')

    return last
