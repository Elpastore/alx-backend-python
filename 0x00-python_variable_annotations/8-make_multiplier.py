#!/usr/bin/env python3
"""
module 8-make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a callable function
    """
    def callable_func(a: float) -> float:
        """
        return the multiplication
        """
        return a * multiplier
    return callable_func
