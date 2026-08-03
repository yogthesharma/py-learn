"""
Real-World Async Patterns (simulated)

This file ties together patterns you will use in production:

  1. asyncio.gather     — parallel independent I/O (API, DB queries)
  2. asyncio.create_task — fire background work, await later
  3. asyncio.wait_for   — timeout slow dependencies
  4. async with         — guaranteed connection cleanup

Everything here is simulated with asyncio.sleep — no real network.
These same shapes appear in FastAPI endpoints, aiohttp clients,
and async database drivers (asyncpg, SQLAlchemy async).

FastAPI note:
  route handlers can be `async def`. The framework runs them on
  the event loop, so await gather / create_task / wait_for /
  async with all work naturally inside a request handler.
"""

from __future__ import annotations

import asyncio
import time
from contextlib import asynccontextmanager
from typing import AsyncIterator, Optional


# ------------------------------------------------------------
# Simulated API clients
# ------------------------------------------------------------
async def fetch_user(user_id: str) -> dict[str, str]:
    await asyncio.sleep(0.3)
    return {"id": user_id, "name": "Yog"}


async def fetch_orders(user_id: str) -> list[str]:
    await asyncio.sleep(0.4)
    return ["order-1", "order-2"]


async def fetch_preferences(user_id: str) -> dict[str, bool]:
    await asyncio.sleep(0.2)
    return {"dark_mode": True}


# ------------------------------------------------------------
# Pattern 1 — gather for parallel API fetches
# ------------------------------------------------------------
async def get_dashboard(user_id: str) -> dict[str, object]:
    started = time.perf_counter()
    user, orders, prefs = await asyncio.gather(
        fetch_user(user_id),
        fetch_orders(user_id),
        fetch_preferences(user_id),
    )
    elapsed = time.perf_counter() - started
    print(f"Dashboard loaded in ~{elapsed:.1f}s (expect ~0.4s)")
    return {"user": user, "orders": orders, "preferences": prefs}


print("--- Pattern 1: gather parallel fetches ---")
asyncio.run(get_dashboard("user-1"))
print()


# ------------------------------------------------------------
# Pattern 2 — create_task for background work
# ------------------------------------------------------------
async def write_audit_log(event: str) -> None:
    await asyncio.sleep(0.3)
    print(f"Audit logged: {event}")


async def process_order(order_id: str) -> str:
    started = time.perf_counter()

    # Start logging in background — do not block the response
    log_task = asyncio.create_task(write_audit_log(f"order:{order_id}"))

    await asyncio.sleep(0.2)  # Simulate order processing
    result = f"processed:{order_id}"

    await log_task  # Ensure log finished before we claim done
    elapsed = time.perf_counter() - started
    print(f"Order result: {result} (~{elapsed:.1f}s)")
    return result


print("--- Pattern 2: create_task background work ---")
asyncio.run(process_order("order-99"))
print()


# ------------------------------------------------------------
# Pattern 3 — timeout around slow I/O
# ------------------------------------------------------------
async def call_external_service() -> str:
    await asyncio.sleep(1.0)
    return "external-ok"


async def call_with_timeout() -> str:
    try:
        return await asyncio.wait_for(call_external_service(), timeout=0.25)
    except asyncio.TimeoutError:
        return "cached-fallback"


async def resilient_endpoint() -> None:
    started = time.perf_counter()
    result = await call_with_timeout()
    elapsed = time.perf_counter() - started
    print(f"Service response: {result} (~{elapsed:.1f}s)")


print("--- Pattern 3: timeout slow I/O ---")
asyncio.run(resilient_endpoint())
print()


# ------------------------------------------------------------
# Pattern 4 — async context manager for connection
# ------------------------------------------------------------
class AsyncDBPool:
    def __init__(self, dsn: str) -> None:
        self.dsn = dsn
        self._conn: Optional[str] = None

    async def __aenter__(self) -> "AsyncDBPool":
        await asyncio.sleep(0.1)
        self._conn = f"pool:{self.dsn}"
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await asyncio.sleep(0.05)
        self._conn = None

    async def execute(self, sql: str) -> list[str]:
        await asyncio.sleep(0.1)
        return [f"row:{sql}"]


@asynccontextmanager
async def get_db() -> AsyncIterator[AsyncDBPool]:
    pool = AsyncDBPool("postgres://localhost/app")
    async with pool as db:
        yield db


async def query_users() -> None:
    async with get_db() as db:
        rows = await db.execute("SELECT * FROM users LIMIT 5")
        print("Query rows:", rows)


print("--- Pattern 4: async context manager ---")
asyncio.run(query_users())
print()


# ------------------------------------------------------------
# Combined — mini "FastAPI-style" handler
# ------------------------------------------------------------
async def handler_get_profile(user_id: str) -> dict[str, object]:
    """Shape of an async FastAPI route — all patterns together."""
    started = time.perf_counter()

    audit = asyncio.create_task(write_audit_log(f"profile_view:{user_id}"))

    async with get_db() as db:
        db_rows = await db.execute(f"SELECT * FROM profiles WHERE id='{user_id}'")

    try:
        user_data = await asyncio.wait_for(fetch_user(user_id), timeout=0.5)
    except asyncio.TimeoutError:
        user_data = {"id": user_id, "name": "Unknown"}

    _, orders = await asyncio.gather(
        audit,
        fetch_orders(user_id),
    )

    elapsed = time.perf_counter() - started
    print(f"Profile handler ~{elapsed:.1f}s")
    return {"user": user_data, "db_rows": db_rows, "orders": orders}


print("--- Combined handler ---")
result = asyncio.run(handler_get_profile("user-42"))
print("Response keys:", list(result.keys()))
print()


# ------------------------------------------------------------
# Where this goes next
# ------------------------------------------------------------
# - FastAPI: async def routes, Depends(), BackgroundTasks
# - aiohttp / httpx: async HTTP client with await client.get(...)
# - asyncpg / SQLAlchemy 2.0: async with engine.connect() as conn
# - websockets: async for message in websocket
#
# The building blocks in 01-09 map directly to these libraries.

print("--- Next steps ---")
print("These patterns map to FastAPI routes and async HTTP/DB libraries.")
print("See 01-09 for each building block in isolation.")
