"""
Context Managers

The magic behind:
  with open(...) as file:

`__enter__` runs at the start of the `with` block.
`__exit__` runs at the end — even if an exception was raised.

That's why files close, locks release, and DB connections clean up
reliably without a manual try/finally everywhere.
"""

from pathlib import Path

DIR = Path(__file__).parent
NOTES = DIR.parent / "06-files-and-json" / "notes.txt"


# ------------------------------------------------------------
# The problem — remember to close (easy to forget)
# ------------------------------------------------------------
file = open(NOTES, encoding="utf-8")
try:
    print(file.read().strip())
finally:
    file.close()
print()


# ------------------------------------------------------------
# The better way — with handles cleanup
# ------------------------------------------------------------
with open(NOTES, encoding="utf-8") as file:
    print(file.read().strip())
print()


# ------------------------------------------------------------
# How — __enter__ / __exit__
# ------------------------------------------------------------
class DatabaseConnection:
    def __enter__(self):
        print("Connected")
        return self  # bound to `as db`

    def __exit__(self, exc_type, exc_value, traceback):
        # Called on success AND on exception
        print("Disconnected")
        # return False / None → exception (if any) still propagates
        # return True → swallow the exception (rare)


with DatabaseConnection() as db:
    print("Querying...", db)
print()


# ------------------------------------------------------------
# __exit__ still runs when an exception occurs
# ------------------------------------------------------------
try:
    with DatabaseConnection():
        print("About to fail...")
        raise ValueError("Oops")
except ValueError as error:
    print("Caller saw:", error)
print()


# ------------------------------------------------------------
# Real backend-ish uses
# ------------------------------------------------------------
# with db.transaction(): ...
# with lock: ...
# with tempfile.TemporaryDirectory() as temp: ...
# with socket.socket(...) as sock: ...


# ------------------------------------------------------------
# Challenge — Timer context manager
# ------------------------------------------------------------
# with Timer():
#     print("Doing some work...")
#
# → Timer started
# → Doing some work...
# → Timer stopped


class Timer:
    def __enter__(self):
        print("Timer started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Timer stopped")


with Timer():
    print("Doing some work...")
