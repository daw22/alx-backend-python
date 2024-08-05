#!/usr/bin/env python3
"""
creates asyncio task
"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    create and returns asyncio task
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
