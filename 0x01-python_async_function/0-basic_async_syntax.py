#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int =10) -> float:
    twait = random.random()*max_delay
    await asyncio.sleep(twait)
    return twait
