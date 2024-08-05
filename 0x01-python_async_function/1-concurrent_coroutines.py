#!/usr/bin/env python3
"""
concurrency in python
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random async function n times
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    res = [await task for task in asyncio.as_completed(tasks)]
    return res
