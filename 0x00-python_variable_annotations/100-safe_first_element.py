#!/usr/bin/env python3
"""
Duck typing a function
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    return first element of None
    """
    if lst:
        return lst[0]
    else:
        return None
