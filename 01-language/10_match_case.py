"""
Structural Pattern Matching (match / case)

Python 3.10+ adds `match` / `case` — a cleaner way to branch on values
and simple structures. It is NOT a drop-in replacement for every if/elif,
but it shines when matching shapes (tuples, dicts, objects) and literals.

This file checks your Python version: match demos run only on 3.10+.
On 3.9 and below, equivalent if/elif logic is shown instead.

Note: match/case is syntax — it cannot appear in this file's source on
Python 3.9 (SyntaxError). The 3.10+ demos use exec() so the file still runs.
"""

from __future__ import annotations

import sys


# ------------------------------------------------------------
# Version check
# ------------------------------------------------------------
HAS_MATCH = sys.version_info >= (3, 10)

if HAS_MATCH:
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor} — running match/case demos."
    )
else:
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor} detected. "
        "match/case requires Python 3.10+. Showing if/elif equivalents instead."
    )
print()


# ------------------------------------------------------------
# Match on simple values
# ------------------------------------------------------------
def describe_http_status(status: int) -> str:
    if status == 200:
        return "OK"
    elif status == 404:
        return "Not Found"
    elif status == 500:
        return "Internal Server Error"
    else:
        return "Unknown status"


if HAS_MATCH:
    exec(
        """
def describe_http_status_match(status: int) -> str:
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
"""
    )
    print("if/elif:", describe_http_status(200), describe_http_status(418))
    print("match:  ", describe_http_status_match(200), describe_http_status_match(418))
else:
    print(describe_http_status(200))
    print(describe_http_status(418))
print()


# ------------------------------------------------------------
# Match with guards (extra conditions)
# ------------------------------------------------------------
def grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


if HAS_MATCH:
    exec(
        """
def grade_match(score: int) -> str:
    match score:
        case s if s >= 90:
            return "A"
        case s if s >= 80:
            return "B"
        case s if s >= 70:
            return "C"
        case s if s >= 60:
            return "D"
        case _:
            return "F"
"""
    )
    print("if/elif:", grade(95), grade(72), grade(55))
    print("match:  ", grade_match(95), grade_match(72), grade_match(55))
else:
    print(grade(95))
    print(grade(72))
    print(grade(55))
print()


# ------------------------------------------------------------
# Match on simple structure (tuple / sequence)
# ------------------------------------------------------------
def describe_point(point: tuple[int, int]) -> str:
    x, y = point
    if x == 0 and y == 0:
        return "origin"
    elif x == 0:
        return f"on y-axis at y={y}"
    elif y == 0:
        return f"on x-axis at x={x}"
    else:
        return f"point at ({x}, {y})"


if HAS_MATCH:
    exec(
        """
def describe_point_match(point: tuple[int, int]) -> str:
    match point:
        case (0, 0):
            return "origin"
        case (0, y):
            return f"on y-axis at y={y}"
        case (x, 0):
            return f"on x-axis at x={x}"
        case (x, y):
            return f"point at ({x}, {y})"
"""
    )
    print("if/elif:", describe_point((0, 0)), describe_point((3, 4)))
    print("match:  ", describe_point_match((0, 0)), describe_point_match((3, 4)))
else:
    print(describe_point((0, 0)))
    print(describe_point((0, 5)))
    print(describe_point((3, 4)))
print()


# ------------------------------------------------------------
# Match on dict structure
# ------------------------------------------------------------
def handle_event(event: dict[str, object]) -> str:
    event_type = event.get("type")
    if event_type == "click" and "x" in event and "y" in event:
        return f"Click at ({event['x']}, {event['y']})"
    elif event_type == "key" and "key" in event:
        return f"Key pressed: {event['key']}"
    elif event_type is not None:
        return f"Unknown event type: {event_type}"
    else:
        return "Malformed event"


if HAS_MATCH:
    exec(
        """
def handle_event_match(event: dict[str, object]) -> str:
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"Click at ({x}, {y})"
        case {"type": "key", "key": key}:
            return f"Key pressed: {key}"
        case {"type": t}:
            return f"Unknown event type: {t}"
        case _:
            return "Malformed event"
"""
    )
    evt = {"type": "click", "x": 10, "y": 20}
    print("if/elif:", handle_event(evt))
    print("match:  ", handle_event_match(evt))
else:
    print(handle_event({"type": "click", "x": 10, "y": 20}))
    print(handle_event({"type": "key", "key": "Enter"}))
print()


# ------------------------------------------------------------
# Challenge — classify_command
# ------------------------------------------------------------
# classify_command("quit")       -> "exit"
# classify_command("help")       -> "show help"
# classify_command("load file")  -> "load: file"
# classify_command("save data")  -> "save: data"
# classify_command("unknown")    -> "unknown command"


def classify_command(text: str) -> str:
    parts = text.split(maxsplit=1)
    if parts == ["quit"]:
        return "exit"
    elif parts == ["help"]:
        return "show help"
    elif len(parts) == 2 and parts[0] == "load":
        return f"load: {parts[1]}"
    elif len(parts) == 2 and parts[0] == "save":
        return f"save: {parts[1]}"
    else:
        return "unknown command"


print(classify_command("quit"))
print(classify_command("load file"))
print(classify_command("save data"))
print(classify_command("unknown"))
