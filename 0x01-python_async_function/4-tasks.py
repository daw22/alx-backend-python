#!/usr/bin/env python3
"""
concurrency in python
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random async function n times
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    res = [await task for task in asyncio.as_completed(tasks)]
    return res
