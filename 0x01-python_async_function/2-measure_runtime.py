#!/usr/bin/env python3
"""
2-measure_runtime. module
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function that mesure the total time
    Args:
        n (int): number of execute time
        max_delay (int): delay for execution

    Returns:
        float: the total time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
