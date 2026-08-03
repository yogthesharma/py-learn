"""
Async Context Managers — async with

The sync `with` statement calls __enter__ / __exit__ on a context manager.
The async version uses `async with` and __aenter__ / __aexit__.

Use async with when setup or teardown involves awaiting I/O:
  - opening/closing a database connection
  - acquiring/releasing a lock
  - starting/stopping a session

contextlib.asynccontextmanager lets you write them with
@asynccontextmanager + yield — same pattern as @contextmanager.
"""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator, Optional


# ------------------------------------------------------------
# Sync vs async — mental model
# ------------------------------------------------------------
# sync:
#   with open("file") as f:
#       f.read()
#
# async:
#   async with connection() as conn:
#       await conn.query(...)
#
# Both guarantee cleanup in __exit__ / __aexit__ even on errors.


# ------------------------------------------------------------
# Fake AsyncDB — class-based async context manager
# ------------------------------------------------------------
class AsyncDB:
    def __init__(self, dsn: str) -> None:
        self.dsn = dsn
        self.connection: Optional[str] = None

    async def __aenter__(self) -> "AsyncDB":
        print(f"Connecting to {self.dsn}...")
        await asyncio.sleep(0.2)
        self.connection = f"conn:{self.dsn}"
        print("Connected")
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        print(f"Closing {self.connection}...")
        await asyncio.sleep(0.1)
        self.connection = None
        print("Closed")

    async def query(self, sql: str) -> list[str]:
        if self.connection is None:
            raise RuntimeError("Not connected")
        await asyncio.sleep(0.1)
        return [f"row-for:{sql}"]


async def use_async_db() -> None:
    async with AsyncDB("postgres://localhost/app") as db:
        rows = await db.query("SELECT * FROM users")
        print("Rows:", rows)
    print("Outside async with — connection cleaned up")


print("--- Fake AsyncDB ---")
asyncio.run(use_async_db())
print()


# ------------------------------------------------------------
# Compare to sync with (conceptual)
# ------------------------------------------------------------
# Sync file open is instant — no await needed.
# AsyncDB connect/close simulate network handshakes — must await.
#
# Rule of thumb:
#   if __enter__ or __exit__ would need await → use async with


# ------------------------------------------------------------
# @asynccontextmanager decorator
# ------------------------------------------------------------
@asynccontextmanager
async def fake_session(user_id: str) -> AsyncIterator[dict[str, str]]:
    print(f"Opening session for {user_id}")
    await asyncio.sleep(0.1)
    session = {"user_id": user_id, "token": "abc123"}
    try:
        yield session
    finally:
        print(f"Revoking token for {user_id}")
        await asyncio.sleep(0.05)


async def use_session() -> None:
    async with fake_session("user-42") as session:
        print("Session:", session)
        await asyncio.sleep(0.1)
        print("Work inside session")


print("--- @asynccontextmanager ---")
asyncio.run(use_session())
print()


# ------------------------------------------------------------
# Cleanup runs even when an error occurs
# ------------------------------------------------------------
async def error_inside_context() -> None:
    try:
        async with AsyncDB("postgres://localhost/app") as db:
            await db.query("SELECT 1")
            raise ValueError("Something went wrong")
    except ValueError as error:
        print("Caught:", error)
    print("Connection still closed via __aexit__")


print("--- Cleanup on error ---")
asyncio.run(error_inside_context())
print()


# ------------------------------------------------------------
# Mini Challenge — AsyncTimer
# ------------------------------------------------------------
# Build an async context manager that prints elapsed time on exit.
# Use time.perf_counter() in __aenter__ / __aexit__ (or decorator).


import time


class AsyncTimer:
    def __init__(self, label: str) -> None:
        self.label = label
        self.start: float = 0.0

    async def __aenter__(self) -> "AsyncTimer":
        self.start = time.perf_counter()
        print(f"{self.label} started")
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        elapsed = time.perf_counter() - self.start
        print(f"{self.label} finished in {elapsed:.2f}s")


async def timed_work() -> None:
    async with AsyncTimer("database migration"):
        await asyncio.sleep(0.3)
        print("Migration step 1 done")
        await asyncio.sleep(0.2)


print("--- Challenge: AsyncTimer ---")
asyncio.run(timed_work())
