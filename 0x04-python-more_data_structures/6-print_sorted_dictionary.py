#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    A function that prints a dictionary by ordered keys
    """
    keys = sorted(a_dictionary.keys())
    for key in keys:
        print(f"{key}: {a_dictionary[key]}")
