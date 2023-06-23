#!/usr/bin/python3

# print_last_digit: Function that print last digit of any number
# Number: Arguments that hold pass variable or value
# last: Holds last digit of passed argument
# Return: Last digit

def print_last_digit(number):
    last = (-1 * number) % 10 if number < 0 else number % 10
    print(f'{last}', end='')

    return last
