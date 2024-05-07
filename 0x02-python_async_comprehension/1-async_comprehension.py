#!/usr/bin/env python3
"""
1-async_comprehension module
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    return a list of yield from async_generator
    """
    yields = [i async for i in async_generator()]

    return yields
