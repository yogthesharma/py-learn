"""
Encapsulation

Hide internal state behind methods. Leading underscore (`_balance`) signals
"private by convention" — Python does not enforce access.

`@property` exposes read-only access without callers touching `_balance`
directly. Validate in `deposit` / `withdraw`.

Use when invariants matter (balances never negative, valid amounts only).

Gotcha: `_name` is still reachable — encapsulation in Python is discipline,
not a hard barrier.
"""

class BankAccount:

    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            print("Invalid Deposit Value")
            return
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid withdrawal amount")
            return

        if amount > self._balance:
            print("Insufficient balance")
            return

        self._balance -= amount


account = BankAccount("Yog")

account.deposit(1000)
account.withdraw(300)

print(account.balance)
