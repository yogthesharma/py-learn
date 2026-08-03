"""
Coroutines

A coroutine is an asynchronous function.

Instead of:

    def greet():

we write:

    async def greet():

But here's the important part...

Calling an async function DOES NOT execute it.

It returns a coroutine object.

Only when the coroutine is awaited (or run by the event loop)
does the function actually start executing.
"""

from __future__ import annotations

import asyncio


# ------------------------------------------------------------
# Normal function
# ------------------------------------------------------------
def greet_sync() -> None:
    print("Hello from sync!")


print("Calling sync function...")
greet_sync()
print()


# ------------------------------------------------------------
# Async function
# ------------------------------------------------------------
async def greet_async() -> None:
    print("Hello from async!")


print("Calling async function...")
result = greet_async()

print(result)
print(type(result))
print()

# Output:
#
# <coroutine object greet_async at 0x...>
#
# Notice:
# Nothing printed from inside greet_async().
#
# Why?
#
# Because calling an async function creates
# a coroutine object.
#
# It does NOT execute it.


# ------------------------------------------------------------
# Running a coroutine
# ------------------------------------------------------------
# Close the unused coroutine from above (avoids RuntimeWarning)
result.close()

asyncio.run(greet_async())
print()


# ------------------------------------------------------------
# Await inside another coroutine
# ------------------------------------------------------------
async def say_name() -> None:
    print("My name is Yog")


async def main() -> None:
    print("Starting...")
    await say_name()
    print("Finished!")


asyncio.run(main())
print()


# ------------------------------------------------------------
# Execution order
# ------------------------------------------------------------
async def task() -> None:
    print("Task started")
    print("Task finished")


async def run_demo() -> None:
    print("Before await")
    await task()
    print("After await")


asyncio.run(run_demo())
print()


# ------------------------------------------------------------
# Key rules
# ------------------------------------------------------------
# 1. async def → returns a coroutine when called
# 2. asyncio.run(...) → starts the event loop (usually once, at the top)
# 3. await → can only be used inside async def
# 4. await pauses THIS coroutine until the awaited one finishes
#    (other tasks can run during real I/O waits — next lessons)


# ------------------------------------------------------------
# Mini Challenge
# ------------------------------------------------------------
# Write async hello() that prints "Hello async world"
# and run it with asyncio.run.


async def hello() -> None:
    print("Hello async world")


asyncio.run(hello())
