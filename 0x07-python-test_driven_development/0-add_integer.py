#!/usr/bin/python3
"""
Add integer model
contains:
add_integer function
"""


def add_integer(a, b=98):
    """
    Adds two integers
    """
    if type(a) if float:
        a = int(a)
    if type(b) if float:
        b = int(b)

    if type(a) is not int or type(a) is float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is float:
        raise TypeError("b must be an integer")
    
    return a + b
