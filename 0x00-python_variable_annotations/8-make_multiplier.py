#!/usr/bin/env python3
"""
Contains make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A type-annotated function that takes a float multiplier
    as argument and returns a function that multiplies a float
    by multiplier
    """
    def func(mult: float) -> float:
        """
        multiplies two floats
        """
        return (multiplier * mult)
    return (func)
