#!/usr/bin/env python3
"""
A type-annotated function
"""


def sum_list(input_list: list[float]) -> float:
    """
    A type-annotated function which takes a list
    of floats as argument and returns their sum
    as a float
    """
    total: float = 0
    for n in input_list:
        total += n
    return (total)
