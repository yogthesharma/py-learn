"""
asyncio.gather

Until now:

    await a()
    await b()
    await c()

was still sequential — one path, sum of waits.

gather schedules several coroutines together so the event loop
can switch between them while they wait.

JS mental model: Promise.all([...]) ≈ asyncio.gather(...)

Important:
  await still suspends the CURRENT coroutine.
  gather gives the event loop MULTIPLE coroutines to interleave.
"""

from __future__ import annotations

import asyncio
import time


# ------------------------------------------------------------
# Three tasks — each waits ~2 seconds
# ------------------------------------------------------------
async def task(name: str, seconds: float) -> str:
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} finished")
    return name


# ------------------------------------------------------------
# Sequential — ~6 seconds
# ------------------------------------------------------------
async def sequential() -> None:
    started = time.perf_counter()
    await task("A", 2)
    await task("B", 2)
    await task("C", 2)
    elapsed = time.perf_counter() - started
    print(f"Sequential ~{elapsed:.1f}s (expect ~6s)")


print("--- Sequential ---")
asyncio.run(sequential())
print()


# ------------------------------------------------------------
# Concurrent with gather — ~2 seconds
# ------------------------------------------------------------
async def concurrent() -> None:
    started = time.perf_counter()
    results = await asyncio.gather(
        task("A", 2),
        task("B", 2),
        task("C", 2),
    )
    elapsed = time.perf_counter() - started
    print("Results:", results)
    print(f"Gather ~{elapsed:.1f}s (expect ~2s)")


print("--- Gather ---")
asyncio.run(concurrent())
print()


# ------------------------------------------------------------
# What changed?
# ------------------------------------------------------------
# gather(...) schedules all three coroutines with the event loop
# and waits until ALL finish.
# While A sleeps, the event loop can run B and C.
# Wall-clock time ≈ longest wait, not the sum.
#
# Timeline (gather):
#
#   Time →
#   0s
#   A ██████████
#   B ██████████
#   C ██████████
#   2s  All finished
#
# Timeline (sequential):
#
#   A ██████████
#               B ██████████
#                           C ██████████
#   Total ≈ 6s
#
# gather ≈ 2s


# ------------------------------------------------------------
# Returning values — order matches INPUT order, not finish order
# ------------------------------------------------------------
# gather returns a list whose positions match the order you passed
# the coroutines — even if a later one finishes first.
# ------------------------------------------------------------
async def fetch(name: str, seconds: float) -> str:
    await asyncio.sleep(seconds)
    return f"data:{name}"


async def ordered_results() -> None:
    # notifications finishes first (0.1s), but unpacking stays:
    # user, orders, notifications
    a, b, c = await asyncio.gather(
        fetch("user", 0.3),
        fetch("orders", 0.2),
        fetch("notifications", 0.1),
    )
    print(a, b, c)


asyncio.run(ordered_results())
print()


# ------------------------------------------------------------
# Real backend — fix the ~0.9s endpoint from 03_await
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


async def endpoint_sequential() -> None:
    started = time.perf_counter()
    user = await get_user()
    orders = await get_orders()
    notifications = await get_notifications()
    elapsed = time.perf_counter() - started
    print(user, orders, notifications)
    print(f"Sequential endpoint ~{elapsed:.1f}s")


async def endpoint_gather() -> None:
    started = time.perf_counter()
    user, orders, notifications = await asyncio.gather(
        get_user(),
        get_orders(),
        get_notifications(),
    )
    elapsed = time.perf_counter() - started
    print(user, orders, notifications)
    print(f"Gather endpoint ~{elapsed:.1f}s (expect ~0.3s)")


print("--- Backend comparison ---")
asyncio.run(endpoint_sequential())
asyncio.run(endpoint_gather())
print()


# ------------------------------------------------------------
# Exceptions — first failure cancels the rest by default
# ------------------------------------------------------------
async def ok() -> str:
    await asyncio.sleep(0.1)
    return "ok"


async def boom() -> str:
    await asyncio.sleep(0.05)
    raise ValueError("Something broke")


async def gather_errors() -> None:
    try:
        await asyncio.gather(ok(), boom())
    except ValueError as error:
        print("Caught:", error)

    # Collect errors instead of raising immediately:
    results = await asyncio.gather(ok(), boom(), return_exceptions=True)
    print("With return_exceptions:", results)


asyncio.run(gather_errors())
print()


# ------------------------------------------------------------
# Mini Challenge
# ------------------------------------------------------------
# cook_rice (2s), cook_dal (2s), make_roti (2s)
# gather them in prepare_dinner()
# Prove total time is ~2s, not ~6s


async def cook_rice() -> str:
    print("Cooking rice...")
    await asyncio.sleep(2)
    print("Rice ready")
    return "rice"


async def cook_dal() -> str:
    print("Cooking dal...")
    await asyncio.sleep(2)
    print("Dal ready")
    return "dal"


async def make_roti() -> str:
    print("Making roti...")
    await asyncio.sleep(2)
    print("Roti ready")
    return "roti"


async def prepare_dinner() -> None:
    print("Starting dinner prep")
    started = time.perf_counter()
    dishes = await asyncio.gather(
        cook_rice(),
        cook_dal(),
        make_roti(),
    )
    elapsed = time.perf_counter() - started
    print("Dishes:", dishes)
    print(f"Dinner ready in ~{elapsed:.1f}s (expect ~2s)")


print("--- Challenge ---")
asyncio.run(prepare_dinner())
