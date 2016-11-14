#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Adding exception handling to an existing function"""


def simple_lookup(var1, var2):
    """Exeption handling with an exisiting function

    Args:
        var1(mixed): Variable 1 of this function
        var2(mixed): Variable 2 of this function

    Returns:
            An exception and var1'

    
    Examples:
            >>> simple_lookup([1,2], 4)
            Warning: Your index/key doesn't exist.
            [1,2]

    """
    
    try:
        return var1[var2]
    except(LookupError):
        print "Warning: Your index/key doesn't exist."
        return var1

