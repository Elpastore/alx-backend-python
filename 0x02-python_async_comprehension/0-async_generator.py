#!/usr/bin/env python3
"""
0-async_generator moddule
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    async_generator function

    This function is an asynchronous generator that yields random
    floating-point numbers between 0 and 10. It uses the asyncio module
    to introduce a delay of 1 second between each yield.

    Returns:
        AsyncGenerator[float, None]: An asynchronous generator that
        yields floating-point numbers.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        # yield random.randint(0, 10)
        yield random.random() * 10
