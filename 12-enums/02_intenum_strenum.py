"""
IntEnum and StrEnum

Specialized enums whose members also behave like ints or strings.

IntEnum — members compare equal to ints and work in arithmetic:
  HttpStatus.OK == 200     → True
  HttpStatus.OK + 1        → 201

StrEnum (Python 3.11+) — members compare equal to str:
  HttpMethod.GET == "GET"  → True
  ", ".join(methods)       → works when methods are StrEnum members

On Python < 3.11, StrEnum is approximated with class HttpMethod(str, Enum).

When to use which:
  Enum     — default; members are NOT interchangeable with raw values
  IntEnum  — HTTP status codes, error codes, numeric flags needing int math
  StrEnum  — API method names, config keys, JSON serialization

Gotcha: IntEnum/StrEnum weaken type safety — HttpStatus.OK == 200 is True.
Prefer plain Enum when you want strict "only these named members" semantics.
"""

from __future__ import annotations

import sys
from enum import Enum, IntEnum, auto


# ------------------------------------------------------------
# IntEnum — integer-compatible members
# ------------------------------------------------------------
class HttpStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500


print(HttpStatus.OK)
print(HttpStatus.OK == 200)       # True — IntEnum compares with int
print(HttpStatus.OK + 1)          # 201
print(int(HttpStatus.NOT_FOUND))  # 404
print()


# ------------------------------------------------------------
# IntEnum with auto — sequential integers
# ------------------------------------------------------------
class ErrorCode(IntEnum):
    VALIDATION = auto()
    AUTH = auto()
    NOT_FOUND = auto()


print(ErrorCode.VALIDATION, ErrorCode.AUTH, ErrorCode.NOT_FOUND)
print()


# ------------------------------------------------------------
# StrEnum — Python 3.11+ or mixin fallback
# ------------------------------------------------------------
if sys.version_info >= (3, 11):
    from enum import StrEnum

    class HttpMethod(StrEnum):
        GET = "GET"
        POST = "POST"
        PUT = "PUT"
        DELETE = "DELETE"
else:
    class HttpMethod(str, Enum):
        GET = "GET"
        POST = "POST"
        PUT = "PUT"
        DELETE = "DELETE"


print(HttpMethod.GET)
print(HttpMethod.GET == "GET")  # True — behaves like str
print(f"Request: {HttpMethod.POST} /users")
print()


# ------------------------------------------------------------
# When to use which
# ------------------------------------------------------------
# Enum     — general named constants (default choice)
# IntEnum  — numeric codes that need int arithmetic/comparison
# StrEnum  — string constants for APIs, config keys, serialization


# ------------------------------------------------------------
# Challenge — HttpMethod as str enum-like
# ------------------------------------------------------------
# methods = [HttpMethod.GET, HttpMethod.POST]
# ", ".join(methods) -> "GET, POST"


methods = [HttpMethod.GET, HttpMethod.POST, HttpMethod.DELETE]
print(", ".join(methods))


def is_read_only(method: HttpMethod) -> bool:
    return method in (HttpMethod.GET,)


print("GET read-only:", is_read_only(HttpMethod.GET))
print("POST read-only:", is_read_only(HttpMethod.POST))
