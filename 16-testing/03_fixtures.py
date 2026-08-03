"""
Fixtures

A fixture provides reusable setup data (or resources) to tests — define
once, inject wherever needed instead of duplicating boilerplate.

pytest syntax:
  @pytest.fixture
  def sample_user():
      return {"name": "Ada", "id": 1}

  def test_greet(sample_user):
      assert greet(sample_user) == "Hello, Ada"

Fixtures can also handle teardown — use yield instead of return:
  @pytest.fixture
  def db():
      conn = connect()
      yield conn
      conn.close()

Scope controls lifetime: function (default), class, module, session.
Use session-scoped fixtures for expensive one-time setup (DB, auth token).

Without pytest, the same idea is a helper function called at the start
of each test — fixtures add dependency injection and automatic cleanup.

Use fixtures for shared test data, connections, temp files, and mocks.
"""

from __future__ import annotations

from typing import Any


# ------------------------------------------------------------
# Manual fixture pattern (no pytest)
# ------------------------------------------------------------
def make_sample_user() -> dict[str, Any]:
    return {"id": 1, "name": "Ada", "email": "ada@example.com"}


def greet(user: dict[str, Any]) -> str:
    return f"Hello, {user['name']}"


print("Manual fixture pattern:")
user = make_sample_user()  # "fixture" created once per test run
assert greet(user) == "Hello, Ada"
print(f"  greet -> {greet(user)}")
print()


# ------------------------------------------------------------
# Setup / teardown idea
# ------------------------------------------------------------
class DatabaseConnection:
    def __init__(self) -> None:
        self.connected = False

    def connect(self) -> None:
        self.connected = True

    def close(self) -> None:
        self.connected = False


def manual_setup_teardown_demo() -> None:
    db = DatabaseConnection()
    db.connect()
    try:
        assert db.connected
        print("  DB connected for test")
    finally:
        db.close()
        print("  DB closed after test")


print("Setup / teardown (try/finally):")
manual_setup_teardown_demo()
print()


# ------------------------------------------------------------
# pytest.fixture (when pytest is available)
# ------------------------------------------------------------
try:
    import pytest

    @pytest.fixture
    def sample_user() -> dict[str, Any]:
        return {"id": 1, "name": "Ada", "email": "ada@example.com"}

    def test_greet_with_fixture(sample_user: dict[str, Any]) -> None:
        assert greet(sample_user) == "Hello, Ada"

    print("pytest.fixture defined: sample_user")
    print("  pytest injects sample_user into test_greet_with_fixture")
    print()
except ImportError:
    print("pytest not installed — fixture decorator skipped")
    print("  concept: def test_x(sample_user): ... uses the fixture return value")
    print()


# ------------------------------------------------------------
# Fixture with teardown — yield form
# ------------------------------------------------------------
try:
    import pytest

    @pytest.fixture
    def db_connection() -> Any:
        db = DatabaseConnection()
        db.connect()
        yield db
        db.close()

    def test_db_is_connected(db_connection: DatabaseConnection) -> None:
        assert db_connection.connected

    print("yield fixture pattern:")
    print("  setup before yield, teardown after test finishes")
    print()
except ImportError:
    pass


# ------------------------------------------------------------
# Challenge — fixture providing sample user dict
# ------------------------------------------------------------
# Create a fixture (or factory) that returns:
#   {"id": 42, "name": "Grace", "role": "admin"}
# Write a test or self-check that user role is "admin".


def make_admin_user() -> dict[str, Any]:
    return {"id": 42, "name": "Grace", "role": "admin"}


def test_admin_role() -> None:
    user = make_admin_user()
    assert user["role"] == "admin"


print("Challenge solution:")
admin = make_admin_user()
print(f"  user: {admin}")
assert admin["role"] == "admin"
print("  role is admin — OK")
