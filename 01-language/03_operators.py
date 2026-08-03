"""
Operators

Arithmetic: `+`, `-`, `*`, `/` (always float), `//` (floor), `%`, `**`.
Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=` — return True/False.
Logical: `and`, `or`, `not` combine conditions.

Use parentheses to make order of operations obvious in formulas
(tax, discounts, unit conversions).

Gotcha: `/` never truncates — use `//` for integer division.
Mixing int and float promotes to float.
"""

salary = int(input("Please provide your monthly salary: "))

monthly_tax = (salary * 10) / 100

print(f"Annual Salary: {salary * 12}")
print(f"Monthly Tax: {monthly_tax}")
print(f"Annual Tax: {monthly_tax * 12}")
print(f"Monthly salary after taxes: {salary - monthly_tax}")