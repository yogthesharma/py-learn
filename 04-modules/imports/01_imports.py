"""
Imports

Bring code from another module into the current namespace.

`from calculator import add` — names must live on PYTHONPATH (same folder
or installed package). `import calculator` then `calculator.add()`.

Use imports to reuse logic and keep files focused; one module per concern.

Gotcha: circular imports (A imports B, B imports A) cause partial loads —
structure shared code into a third module or lazy-import inside functions.
"""

from calculator import add, divide, multiply, subtract

a = 10
b = 5


print(add(a, b))
print(divide(a, b))
print(multiply(a, b))
print(subtract(a, b))
