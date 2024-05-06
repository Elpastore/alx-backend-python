#!/usr/bin/env python3
"""
0-basic_async_syntax module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """function that wait for a certain delay before execution

    Args:
        max_delay (int): the maximum delay ti wait in second

    Returns:
        int: delay to wait
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay
