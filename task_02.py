#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    pass

def get_age(birthyear):
    """ A function to test if a person has a valid age

    Args:
        birthyear(int): The birth year of the person in question

    Returns:
        Age(int): Derrived by subtracting current year minus birth year

    Example:
        >>> get_age(2099)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        __main__.InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear

    if age > 0:
        raise InvalidAgeError
    return age
