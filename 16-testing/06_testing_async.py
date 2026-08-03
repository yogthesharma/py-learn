"""
Testing Async Code

Async functions need an event loop to run — calling them like normal
functions returns a coroutine object, not the result.

Options:
  1. pytest-asyncio — @pytest.mark.asyncio on async def test_...
  2. asyncio.run(coro) inside a normal def test_... (no plugin needed)

  @pytest.mark.asyncio
  async def test_add():
      assert await async_add(2, 3) == 5

Install: pip install pytest pytest-asyncio

asyncio.run wrapper pattern (works in any script or sync test):
  result = asyncio.run(my_async_func())

When to use which:
  pytest-asyncio — standard for test suites; await directly in tests
  asyncio.run    — quick scripts, libraries without pytest, minimal setup

Gotcha: do not call asyncio.run() inside an already-running event loop —
you get RuntimeError. Test gather/timeouts the same way: await in async
tests, or asyncio.run() from sync wrappers.
"""

from __future__ import annotations

import asyncio
from typing import Any


# ------------------------------------------------------------
# Async code under test
# ------------------------------------------------------------
async def async_add(a: int, b: int) -> int:
    await asyncio.sleep(0)  # yield control — simulates I/O
    return a + b


async def fetch_all(urls: list[str]) -> list[str]:
    async def fetch_one(url: str) -> str:
        await asyncio.sleep(0.01)
        return f"body:{url}"

    return list(await asyncio.gather(*(fetch_one(u) for u in urls)))


# ------------------------------------------------------------
# Demo without pytest — asyncio.run wrapper
# ------------------------------------------------------------
def run_async(coro: Any) -> Any:
    return asyncio.run(coro)


print("asyncio.run demo:")
result = run_async(async_add(2, 3))
print(f"  async_add(2, 3) = {result}")
assert result == 5
print()


# ------------------------------------------------------------
# Test async_add with asyncio.run (no plugin needed)
# ------------------------------------------------------------
def test_async_add_sync_wrapper() -> None:
    assert run_async(async_add(10, 5)) == 15


print("Sync wrapper test:")
test_async_add_sync_wrapper()
print("  test_async_add_sync_wrapper passed")
print()


# ------------------------------------------------------------
# gather in a test
# ------------------------------------------------------------
def test_fetch_all() -> None:
    bodies = run_async(fetch_all(["/a", "/b"]))
    assert bodies == ["body:/a", "body:/b"]


print("gather test:")
test_fetch_all()
print("  test_fetch_all passed")
print()


# ------------------------------------------------------------
# pytest-asyncio (when available)
# ------------------------------------------------------------
try:
    import pytest

    @pytest.mark.asyncio
    async def test_async_add_pytest() -> None:
        assert await async_add(7, 8) == 15

    @pytest.mark.asyncio
    async def test_fetch_all_pytest() -> None:
        result = await fetch_all(["/x"])
        assert result == ["body:/x"]

    print("pytest-asyncio tests defined:")
    print("  @pytest.mark.asyncio async def test_...()")
    print("  run with: pytest 16-testing/06_testing_async.py -v")
    print()
except ImportError:
    print("pytest not installed — async tests use asyncio.run wrapper only")
    print()


# ------------------------------------------------------------
# Challenge — test an async add
# ------------------------------------------------------------
# Test async_add(-1, 1) == 0 and async_add(0, 0) == 0


async def challenge_async_add_tests() -> None:
    assert await async_add(-1, 1) == 0
    assert await async_add(0, 0) == 0


print("Challenge solution:")
run_async(challenge_async_add_tests())
print("  async_add edge cases passed")
