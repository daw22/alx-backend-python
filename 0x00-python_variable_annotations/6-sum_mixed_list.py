#!/usr/bin/env python3
"""
mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    A type-annotated function which takes a list
    of integers and floats and returns their sum
    as a float
    """
    return (sum(mxd_lst))
