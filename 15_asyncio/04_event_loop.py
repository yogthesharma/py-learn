"""
The Event Loop

The event loop is the "manager" of asynchronous programs.

Its job is simple:

1. Start coroutines.
2. Watch for operations that are waiting (I/O).
3. While one coroutine waits, run another.
4. Resume suspended coroutines when they're ready.

Think of it as a project manager.

It doesn't do the work itself.
It decides WHO gets CPU time next.

Simplified forever-loop idea:

    while True:
        check_ready_tasks()
        run_one_task()
        check_finished_io()
        resume_waiting_tasks()
"""

from __future__ import annotations

import asyncio
import time


# ------------------------------------------------------------
# One coroutine — nothing surprising yet
# ------------------------------------------------------------
async def download_file() -> None:
    print("Downloading...")
    await asyncio.sleep(2)
    print("Download finished")


async def main() -> None:
    print("Program started")
    await download_file()
    print("Program finished")


asyncio.run(main())
print()


# ------------------------------------------------------------
# What actually happens at await?
# ------------------------------------------------------------
# NOT: program freezes the whole thread and "just waits".
#
# Instead:
#   Coroutine → "I'm waiting."
#   Event loop → "Okay, I'll come back later."
#   Event loop → runs something else (if anything else exists)
#
# Teacher analogy:
#   Student A needs 5 minutes → teacher helps Student B and C
#   Student A raises hand → teacher returns
#
# That switching is cooperative multitasking.
# Every coroutine voluntarily yields with `await`.


# ------------------------------------------------------------
# Waiting marks the coroutine as suspended
# ------------------------------------------------------------
async def wash_clothes() -> None:
    print("Washing...")
    await asyncio.sleep(1)  # "I'm blocked. Come back later."
    print("Finished washing")


asyncio.run(wash_clothes())
print()


# ------------------------------------------------------------
# Important — not true parallelism of Python lines
# ------------------------------------------------------------
# The event loop never executes two Python lines at the
# exact same instant. It switches between coroutines:
#
#   A waiting → B waiting → C ready → A resumes
#
# One thread, many suspended/ready coroutines.


# ------------------------------------------------------------
# Experiment — still sequential (event loop has nothing else)
# ------------------------------------------------------------
async def first() -> None:
    print("First started")
    await asyncio.sleep(2)
    print("First finished")


async def second() -> None:
    print("Second started")
    await asyncio.sleep(1)
    print("Second finished")


async def sequential() -> None:
    print("Main started")
    started = time.perf_counter()

    await first()  # Don't even start second until first completes.
    await second()

    elapsed = time.perf_counter() - started
    print("Main finished")
    print(f"Elapsed ~{elapsed:.1f}s (expect ~3s)")


asyncio.run(sequential())
print()


# ------------------------------------------------------------
# Event Loop ≠ Concurrency by itself
# ------------------------------------------------------------
# The event loop CAN run multiple coroutines —
# but only if multiple coroutines are scheduled.
#
# await first(); await second()
# is still ONE active path. Nothing else to switch to.
#
# Real concurrency comes when we schedule several at once
# (asyncio.gather / create_task) — next lesson.


# ------------------------------------------------------------
# Real backend intuition
# ------------------------------------------------------------
# await database.fetch_user()  → suspend ~300ms
# event loop serves another HTTP request meanwhile
# OS notifies when DB is done → event loop resumes → return JSON


# ------------------------------------------------------------
# Mini Challenge — answers
# ------------------------------------------------------------
# 1. What is the job of the event loop?
#    Schedule coroutines: start them, notice waits, run others,
#    resume when I/O / timers are ready.
#
# 2. Who resumes a suspended coroutine?
#    The event loop (when the waited-on operation completes).
#
# 3. Does the event loop execute two Python functions at once?
#    No — one at a time; it switches between them.
#
# 4. Why doesn't await first(); await second() create concurrency?
#    Because second isn't started until first fully finishes —
#    only one active path is scheduled.

print("--- Mini Challenge answers ---")
print("1. Schedule / resume coroutines around waits.")
print("2. The event loop resumes them.")
print("3. No — cooperative switching, one at a time.")
print("4. second never starts until first is done — one path only.")
