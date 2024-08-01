#!/usr/bin/env python3
"""
more Type annotations
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Generic typing
    """
    if key in dct:
        return dct[key]
    else:
        return default
