#!/usr/bin/env python3
"""
Parallel cmprehensions
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    run async_comprhension four times with asyncio.gather
    measure the total runtime and return it
    """
    start = time.perf_counter()
    calls = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*calls)
    end = time.perf_counter()
    return end - start
