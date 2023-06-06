#!/usr/bin/python3
"""Defines an interger 0 module"""


def add_interger(a, b=98):
    """return the addition of two intergers
       float arguments are typecatsed into intergers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an interger")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an interger")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a+b
