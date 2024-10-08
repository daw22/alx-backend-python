#!/usr/bin/env python3
"""
mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A type-annotated function which takes a list
    of integers and floats and returns their sum
    as a float
    """
    return float(sum(mxd_lst))
