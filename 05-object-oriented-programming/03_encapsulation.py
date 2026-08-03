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
