#!/usr/bin/env python3
"""
Complex type anntation
"""
from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A type-annotated function that takes a string k
    and an int OR float v as arguments and returns
    a tuple
    """
    return ((k, v**2))
