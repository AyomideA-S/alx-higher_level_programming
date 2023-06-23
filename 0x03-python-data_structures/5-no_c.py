#!/usr/bin/python3

def no_c(my_string):
    noc = []
    [noc.append(c) for c in my_string if c not in ['c', 'C']]
    return ''.join(noc)
