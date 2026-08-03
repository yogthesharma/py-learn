"""
Package entry script

Demonstrates importing from a nested package: `utils.calculator` and
`utils.string_utils`. Run from the `packages/` directory.
"""

from utils.calculator import add
from utils.string_utils import to_lower


a, b = 10, 5
name = "Yog Sharma"

print(add(a, b))
print(to_lower(name))
