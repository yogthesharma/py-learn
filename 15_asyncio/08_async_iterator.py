"""
Async Iterators — async for

Sync iteration: for item in iterable → __iter__ / __next__ / StopIteration
Async iteration: async for item in aiter → __aiter__ / __anext__ / StopAsyncIteration

Use async for when producing or consuming items involves awaiting:
  - streaming rows from a database cursor
  - reading websocket messages
  - paginating an API one page at a time

Async generators (async def + yield) are the easiest way to build
async iterables — Python provides __aiter__ / __anext__ for you.
"""

from __future__ import annotations

import asyncio
from typing import AsyncIterator, Optional


# ------------------------------------------------------------
# Class-based async iterator
# ------------------------------------------------------------
class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __aiter__(self) -> "Countdown":
        return self

    async def __anext__(self) -> int:
        if self.current <= 0:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        value = self.current
        self.current -= 1
        return value


async def consume_countdown() -> None:
    print("Countdown:", end=" ")
    async for n in Countdown(5):
        print(n, end=" ")
    print()


print("--- Class async iterator ---")
asyncio.run(consume_countdown())
print()


# ------------------------------------------------------------
# StopAsyncIteration — signals "no more items"
# ------------------------------------------------------------
# Same role as StopIteration in sync code.
# async for catches StopAsyncIteration automatically — you rarely
# call __anext__ by hand unless building custom iteration logic.


# ------------------------------------------------------------
# Async generator — async def + yield
# ------------------------------------------------------------
async def ticker(label: str, count: int, delay: float) -> AsyncIterator[str]:
    for i in range(count):
        await asyncio.sleep(delay)
        yield f"{label}-{i}"


async def consume_ticker() -> None:
    async for tick in ticker("ping", 4, 0.1):
        print(tick)


print("--- Async generator ---")
asyncio.run(consume_ticker())
print()


# ------------------------------------------------------------
# Streaming pattern — fake paginated API
# ------------------------------------------------------------
async def fetch_page(page: int) -> list[str]:
    await asyncio.sleep(0.1)
    if page > 3:
        return []
    return [f"item-{page}-{i}" for i in range(2)]


async def stream_all_pages() -> AsyncIterator[str]:
    page = 1
    while True:
        rows = await fetch_page(page)
        if not rows:
            break
        for row in rows:
            yield row
        page += 1


async def print_stream() -> None:
    async for item in stream_all_pages():
        print(item)


print("--- Paginated stream ---")
asyncio.run(print_stream())
print()


# ------------------------------------------------------------
# Manual __anext__ (for understanding)
# ------------------------------------------------------------
async def manual_next() -> None:
    countdown = Countdown(3)
    iterator = countdown.__aiter__()
    print(await iterator.__anext__())
    print(await iterator.__anext__())
    print(await iterator.__anext__())
    try:
        await iterator.__anext__()
    except StopAsyncIteration:
        print("StopAsyncIteration — done")


print("--- Manual __anext__ ---")
asyncio.run(manual_next())
print()


# ------------------------------------------------------------
# Mini Challenge — countdown async iterator
# ------------------------------------------------------------
# Implement CountdownTimer(n) that async-for yields n, n-1, ... 1
# with a short delay between each. Print "Go!" after the loop.


class CountdownTimer:
    def __init__(self, start: int, delay: float = 0.1) -> None:
        self.start = start
        self.delay = delay
        self._current: Optional[int] = None

    def __aiter__(self) -> "CountdownTimer":
        self._current = self.start
        return self

    async def __anext__(self) -> int:
        if self._current is None or self._current <= 0:
            raise StopAsyncIteration
        await asyncio.sleep(self.delay)
        value = self._current
        self._current -= 1
        return value


async def launch_countdown() -> None:
    async for n in CountdownTimer(3):
        print(n)
    print("Go!")


print("--- Challenge: CountdownTimer ---")
asyncio.run(launch_countdown())
