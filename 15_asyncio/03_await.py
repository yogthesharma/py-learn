"""
await

The await keyword can only be used inside an async function.

When Python reaches an await:

1. Suspend the current coroutine.
2. Let the event loop run other work.
3. Resume this coroutine once the awaited operation finishes.

await is the point where a coroutine voluntarily gives
control back to the event loop.

Important:

await does NOT automatically create concurrency.
It simply waits for another coroutine.

(JS note: async/await maps closely to Python.
 Promise ≈ coroutine; Promise.all ≈ asyncio.gather.
 Difference: Python needs asyncio.run() to start the event loop.)
"""

from __future__ import annotations

import asyncio
import time


# ------------------------------------------------------------
# Basic await — still sequential
# ------------------------------------------------------------
# asyncio.sleep() is NON-BLOCKING.
# While this coroutine waits, the event loop can execute other coroutines.
#
# Compare:
#   time.sleep()     → blocks the whole thread
#   asyncio.sleep()  → suspends only the current coroutine
# ------------------------------------------------------------
async def make_coffee() -> None:
    print("Brewing coffee...")
    await asyncio.sleep(2)
    print("Coffee ready!")


async def morning() -> None:
    print("Wake up")
    await make_coffee()  # Suspend this coroutine until make_coffee() completes.
    print("Drink coffee")


asyncio.run(morning())
print()


# ------------------------------------------------------------
# Returning values — like value = func(), but with await
# ------------------------------------------------------------
async def calculate_tax() -> float:
    await asyncio.sleep(1)
    return 42.5


async def tax_main() -> None:
    tax = await calculate_tax()
    print(tax)


asyncio.run(tax_main())
print()


# ------------------------------------------------------------
# Multiple awaits — STILL sequential (~2 seconds total)
# ------------------------------------------------------------
async def task_one() -> None:
    print("Task 1")
    await asyncio.sleep(1)


async def task_two() -> None:
    print("Task 2")
    await asyncio.sleep(1)


async def sequential_main() -> None:
    started = time.perf_counter()
    await task_one()
    await task_two()
    elapsed = time.perf_counter() - started
    print(f"Elapsed ~{elapsed:.1f}s (expect ~2s)")


asyncio.run(sequential_main())
print()


# ------------------------------------------------------------
# Surprising but true
# ------------------------------------------------------------
# await first()
# await second()
# await third()
#
# is still first → second → third (one after another).
#
# Real concurrency needs asyncio.gather() — next lesson.


# ------------------------------------------------------------
# Real backend-ish — three awaits ≈ sum of waits
# ------------------------------------------------------------
async def get_user() -> str:
    await asyncio.sleep(0.3)
    return "Yog"


async def get_orders() -> list[str]:
    await asyncio.sleep(0.3)
    return ["order-1", "order-2"]


async def get_notifications() -> list[str]:
    await asyncio.sleep(0.3)
    return ["Welcome!"]


async def endpoint() -> None:
    started = time.perf_counter()
    user = await get_user()
    orders = await get_orders()
    notifications = await get_notifications()
    elapsed = time.perf_counter() - started
    print(user, orders, notifications)
    print(f"Endpoint ~{elapsed:.1f}s (expect ~0.9s)")


asyncio.run(endpoint())
print()


# ------------------------------------------------------------
# Mini Challenge
# ------------------------------------------------------------
# cook_rice → sleep 2 → return "rice"
# dinner awaits it and prints the result


async def cook_rice() -> str:
    print("Cooking rice...")
    await asyncio.sleep(2)
    print("Rice ready!")
    return "rice"


async def dinner() -> None:
    print("Starting dinner")
    food = await cook_rice()
    print(food)
    print("Dinner served!")


asyncio.run(dinner())
