"""
asyncio.create_task vs await

await suspends until something finishes — but it also means
you cannot do other work until that await completes.

create_task schedules a coroutine on the event loop immediately
and returns a Task handle. The work starts in the background;
you await the Task later when you need the result.

JS mental model:
  create_task(coro) ≈ fire-and-forget with a Promise you can await later
  gather(...)       ≈ Promise.all — schedule several and wait for all

Key difference from gather:
  create_task gives you fine-grained control — start work early,
  do other things, await when ready. gather is "schedule all now,
  wait for all at once."
"""

from __future__ import annotations

import asyncio
import time


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------
async def download(name: str, seconds: float) -> str:
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} finished")
    return f"file:{name}"


# ------------------------------------------------------------
# await alone — work starts only when you reach the line
# ------------------------------------------------------------
async def await_only() -> None:
    print("Doing setup...")
    await asyncio.sleep(0.2)
    print("Setup done — now starting download")
    result = await download("report", 0.5)
    print("Got:", result)


print("--- await only (download starts late) ---")
asyncio.run(await_only())
print()


# ------------------------------------------------------------
# create_task — start work in background, await later
# ------------------------------------------------------------
async def create_task_demo() -> None:
    print("Doing setup...")
    # Schedule download NOW — it runs while we do setup.
    task = asyncio.create_task(download("report", 0.5))

    await asyncio.sleep(0.2)
    print("Setup done — download may already be running")

    result = await task  # Wait only if not finished yet
    print("Got:", result)


print("--- create_task (download starts early) ---")
asyncio.run(create_task_demo())
print()


# ------------------------------------------------------------
# JS Promise parallel — start multiple, await later
# ------------------------------------------------------------
async def promise_parallel() -> None:
    started = time.perf_counter()

    # Like: const p1 = fetch(...); const p2 = fetch(...);
    t_user = asyncio.create_task(download("user", 0.3))
    t_orders = asyncio.create_task(download("orders", 0.4))

    print("Both tasks running in background...")
    await asyncio.sleep(0.1)
    print("Doing unrelated work while downloads run")

    user = await t_user
    orders = await t_orders
    elapsed = time.perf_counter() - started
    print(user, orders)
    print(f"Total ~{elapsed:.1f}s (expect ~0.4s, not ~0.7s)")


print("--- JS-style parallel with create_task ---")
asyncio.run(promise_parallel())
print()


# ------------------------------------------------------------
# gather vs create_task — same wall-clock, different control
# ------------------------------------------------------------
async def with_gather() -> None:
    started = time.perf_counter()
    a, b = await asyncio.gather(
        download("A", 0.3),
        download("B", 0.3),
    )
    elapsed = time.perf_counter() - started
    print("gather results:", a, b)
    print(f"gather ~{elapsed:.1f}s")


async def with_create_task() -> None:
    started = time.perf_counter()
    ta = asyncio.create_task(download("A", 0.3))
    tb = asyncio.create_task(download("B", 0.3))
    a = await ta
    b = await tb
    elapsed = time.perf_counter() - started
    print("create_task results:", a, b)
    print(f"create_task ~{elapsed:.1f}s")


print("--- gather vs create_task (both ~0.3s) ---")
asyncio.run(with_gather())
asyncio.run(with_create_task())
print()


# ------------------------------------------------------------
# When create_task shines — start early, await late
# ------------------------------------------------------------
async def slow_validation() -> bool:
    await asyncio.sleep(0.4)
    return True


async def fetch_data() -> str:
    await asyncio.sleep(0.4)
    return "payload"


async def start_early() -> None:
    started = time.perf_counter()

    # Start both immediately
    validation = asyncio.create_task(slow_validation())
    data = asyncio.create_task(fetch_data())

    # Could do more work here while both run...
    await asyncio.sleep(0.1)
    print("Checked config while tasks ran")

    ok = await validation
    payload = await data
    elapsed = time.perf_counter() - started
    print(ok, payload)
    print(f"Parallel start ~{elapsed:.1f}s (expect ~0.4s)")


print("--- start early, await late ---")
asyncio.run(start_early())
print()


# ------------------------------------------------------------
# Task cancellation basics
# ------------------------------------------------------------
async def long_job() -> None:
    try:
        print("long_job: starting")
        await asyncio.sleep(5)
        print("long_job: finished (should not print if cancelled)")
    except asyncio.CancelledError:
        print("long_job: cancelled — cleaning up")
        raise  # Always re-raise CancelledError


async def cancel_demo() -> None:
    task = asyncio.create_task(long_job())
    await asyncio.sleep(0.2)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Caller saw CancelledError after await")


print("--- Task cancellation ---")
asyncio.run(cancel_demo())
print()


# ------------------------------------------------------------
# Mini Challenge
# ------------------------------------------------------------
# Start 3 background tasks with create_task, do other work,
# then await all three. Prove total time ~ longest task, not sum.


async def job(name: str, seconds: float) -> str:
    print(f"{name} running")
    await asyncio.sleep(seconds)
    print(f"{name} done")
    return name


async def run_three_background() -> None:
    started = time.perf_counter()

    t1 = asyncio.create_task(job("alpha", 0.5))
    t2 = asyncio.create_task(job("beta", 0.3))
    t3 = asyncio.create_task(job("gamma", 0.4))

    print("All three started — doing other work")
    await asyncio.sleep(0.1)
    print("Other work done — awaiting results")

    results = await asyncio.gather(t1, t2, t3)
    elapsed = time.perf_counter() - started
    print("Results:", results)
    print(f"Total ~{elapsed:.1f}s (expect ~0.5s, not ~1.2s)")


print("--- Challenge ---")
asyncio.run(run_three_background())
