#!/usr/bin/env python3
"""
A type-annotated function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A type-annotated function which takes a list
    of floats as argument and returns their sum
    as a float
    """
    return (sum(input_list))
