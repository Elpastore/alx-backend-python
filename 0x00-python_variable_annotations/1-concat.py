#!/usr/bin/env python3
"""
module 1-concat
"""


def concat(str1: str, str2: str) -> str:
    """
    concatenate two string
    """
    # concate: str = str1 + str2
    concate: str = "".join([str1, str2])
    return concate
