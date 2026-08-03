"""
Mocking

Replace real dependencies with controlled fakes so unit tests run fast,
deterministically, and without side effects (HTTP, email, filesystem).

unittest.mock (stdlib):
  MagicMock  — fake object; any attribute/method returns another mock
  patch      — temporarily replace a name during a test

  fake = MagicMock()
  fake.get.return_value = {"name": "Ada"}
  fetch_user_name(fake, 1)  → uses fake response, no real HTTP

  with patch("mymodule.time.sleep"):
      ...  # sleep is a no-op inside the block

Why mock:
  Isolate the unit under test from slow or flaky external services
  Simulate edge cases (timeouts, 500 errors) without real infrastructure
  Verify your code calls dependencies correctly (assert_called_with)

Use mocks at system boundaries (API clients, DB, clock, filesystem).
Do not mock the code you are actually testing — mock its dependencies.
"""

from __future__ import annotations

import time
from typing import Any
from unittest.mock import MagicMock, patch


# ------------------------------------------------------------
# Code that depends on external services
# ------------------------------------------------------------
def fetch_user_name(api_client: Any, user_id: int) -> str:
    response = api_client.get(f"/users/{user_id}")
    return response["name"]


def slow_report() -> str:
    time.sleep(2)
    return "done"


print("Why mock:")
print("  - real HTTP calls are slow and flaky in unit tests")
print("  - sleep(2) makes every test run painful")
print("  - mocks let you test YOUR logic in isolation")
print()


# ------------------------------------------------------------
# MagicMock basics
# ------------------------------------------------------------
fake_api = MagicMock()
fake_api.get.return_value = {"name": "Ada", "id": 1}

name = fetch_user_name(fake_api, 1)
print("MagicMock demo:")
print(f"  fetch_user_name(fake_api, 1) -> {name!r}")
assert name == "Ada"
fake_api.get.assert_called_once_with("/users/1")
print("  fake_api.get was called with /users/1")
print()


# ------------------------------------------------------------
# patch — replace during a test
# ------------------------------------------------------------
print("patch demo (mock time.sleep):")


def run_without_sleep() -> None:
    with patch("time.sleep"):
        result = slow_report()
        assert result == "done"
        print("  slow_report() returned without waiting 2 seconds")


run_without_sleep()
print()


# ------------------------------------------------------------
# Mock an API call with patch
# ------------------------------------------------------------
def fetch_status_code(client: Any) -> int:
    return client.get("/health").status_code


print("Mock API status code:")
mock_client = MagicMock()
mock_client.get.return_value.status_code = 200
assert fetch_status_code(mock_client) == 200
print("  status_code == 200  OK")
print()


# ------------------------------------------------------------
# Discoverable tests
# ------------------------------------------------------------
def test_fetch_user_name() -> None:
    client = MagicMock()
    client.get.return_value = {"name": "Grace"}
    assert fetch_user_name(client, 42) == "Grace"


def test_slow_report_patched() -> None:
    with patch("time.sleep"):
        assert slow_report() == "done"


# ------------------------------------------------------------
# Challenge — mock time.sleep or fake HTTP GET
# ------------------------------------------------------------
# Verify slow_report completes quickly when sleep is mocked.
# Verify a fake GET returns expected JSON.


def fake_http_get(url: str) -> dict[str, Any]:
    client = MagicMock()
    if url == "/users/1":
        client.get.return_value = {"id": 1, "name": "Test User"}
    else:
        client.get.return_value = {}
    return client.get(url)


print("Challenge solution:")
with patch("time.sleep"):
    start = time.perf_counter()
    assert slow_report() == "done"
    elapsed = time.perf_counter() - start
    print(f"  slow_report with mocked sleep took {elapsed:.4f}s")

data = fake_http_get("/users/1")
assert data["name"] == "Test User"
print(f"  fake GET /users/1 -> {data}")
