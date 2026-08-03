"""
Timeouts — asyncio.wait_for

wait_for(coro, timeout) runs a coroutine but raises asyncio.TimeoutError
if it does not finish within the given seconds.

Essential for:
  - preventing hung HTTP / DB calls from blocking forever
  - enforcing SLAs on slow dependencies
  - failing fast when a service is down

asyncio.shield(task) protects a task from cancellation when the
outer wait is cancelled — useful when you started work you do not
want lost, but use sparingly (the task may outlive its caller).
"""

from __future__ import annotations

import asyncio
import time


# ------------------------------------------------------------
# Basic wait_for — success within timeout
# ------------------------------------------------------------
async def fast_task() -> str:
    await asyncio.sleep(0.2)
    return "done"


async def success_within_timeout() -> None:
    result = await asyncio.wait_for(fast_task(), timeout=1.0)
    print("Result:", result)


print("--- Success within timeout ---")
asyncio.run(success_within_timeout())
print()


# ------------------------------------------------------------
# TimeoutError — task took too long
# ------------------------------------------------------------
async def slow_task() -> str:
    await asyncio.sleep(2.0)
    return "too late"


async def timeout_demo() -> None:
    try:
        await asyncio.wait_for(slow_task(), timeout=0.3)
    except asyncio.TimeoutError:
        print("Timed out — slow_task did not finish in 0.3s")


print("--- TimeoutError ---")
asyncio.run(timeout_demo())
print()


# ------------------------------------------------------------
# Timing proof — fail fast instead of waiting forever
# ------------------------------------------------------------
async def compare_with_without_timeout() -> None:
    started = time.perf_counter()
    try:
        await asyncio.wait_for(slow_task(), timeout=0.2)
    except asyncio.TimeoutError:
        pass
    with_timeout = time.perf_counter() - started

    started = time.perf_counter()
    # Simulating "would take 2s" — we skip actually waiting
    print("(Without timeout, slow_task would block ~2s)")
    without_timeout_estimate = 2.0

    print(f"With timeout ~{with_timeout:.1f}s")
    print(f"Without timeout ~{without_timeout_estimate:.1f}s (estimated)")


print("--- Fail fast ---")
asyncio.run(compare_with_without_timeout())
print()


# ------------------------------------------------------------
# Timeout on one of several tasks
# ------------------------------------------------------------
async def fetch(name: str, seconds: float) -> str:
    await asyncio.sleep(seconds)
    return f"data:{name}"


async def fetch_with_timeout(name: str, seconds: float, limit: float) -> str:
    try:
        return await asyncio.wait_for(fetch(name, seconds), timeout=limit)
    except asyncio.TimeoutError:
        return f"timeout:{name}"


async def mixed_fetches() -> None:
    results = await asyncio.gather(
        fetch_with_timeout("fast", 0.1, 0.5),
        fetch_with_timeout("slow", 1.0, 0.2),
        fetch_with_timeout("medium", 0.3, 0.5),
    )
    print("Results:", results)


print("--- Timeout per fetch ---")
asyncio.run(mixed_fetches())
print()


# ------------------------------------------------------------
# asyncio.shield — brief mention
# ------------------------------------------------------------
# shield protects the inner task from cancellation when the
# outer wait_for times out or is cancelled.
#
#   task = asyncio.create_task(important_write())
#   await asyncio.shield(task)
#
# If the shielded wait is cancelled, important_write keeps running.
# You lose easy access to its result — handle with care.


async def shield_mention() -> None:
    async def background_save() -> None:
        try:
            print("save: started")
            await asyncio.sleep(0.5)
            print("save: finished")
        except asyncio.CancelledError:
            print("save: cancelled")
            raise

    task = asyncio.create_task(background_save())
    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=0.1)
    except asyncio.TimeoutError:
        print("Outer wait timed out, but shielded save continues")
        await task  # Wait for the protected work


print("--- shield (brief) ---")
asyncio.run(shield_mention())
print()


# ------------------------------------------------------------
# Mini Challenge — timeout a slow task
# ------------------------------------------------------------
# Wrap a 1-second job with wait_for(timeout=0.25).
# Catch TimeoutError and return a fallback string.


async def slow_job() -> str:
    await asyncio.sleep(1.0)
    return "success"


async def fetch_with_fallback() -> str:
    try:
        return await asyncio.wait_for(slow_job(), timeout=0.25)
    except asyncio.TimeoutError:
        return "fallback: service unavailable"


async def challenge() -> None:
    started = time.perf_counter()
    result = await fetch_with_fallback()
    elapsed = time.perf_counter() - started
    print("Result:", result)
    print(f"Returned in ~{elapsed:.1f}s (expect ~0.25s, not ~1s)")


print("--- Challenge ---")
asyncio.run(challenge())
