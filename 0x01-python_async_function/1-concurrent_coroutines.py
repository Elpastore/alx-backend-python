#!/usr/bin/env python3
"""
1-concurrent_coroutines module
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: float) -> List[float]:
    """execute and return the list of all the delays (

    Args:
        n (int): _description_
        max_delay (float): delay return for function to be executed

    Returns:
        List: list of delay in ascending order
    """
    tasks = []
    delays = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for delay in asyncio.as_completed(tasks):
        delays.append(await delay)

    return delays
