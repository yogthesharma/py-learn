"""
String utilities submodule (packages lesson)

Small string helpers (`to_upper`, `to_lower`) consumed by `main.py`
via `from utils.string_utils import to_lower`.
"""

def to_upper(a: str):
    return a.upper()


def to_lower(a: str):
    return a.lower()


if __name__ == "__main__":
    print("String Utils Started")
