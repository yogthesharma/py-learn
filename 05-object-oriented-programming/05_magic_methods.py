"""
Magic Methods (dunder methods)

Methods that start and end with double underscores:
  __init__, __str__, __repr__, __len__, __eq__, __add__, ...

You've already used __init__ — Python calls it when you create an object.

They let YOUR classes work with Python's normal syntax:
  print(obj)  →  obj.__str__()
  len(obj)    →  obj.__len__()
  a == b      →  a.__eq__(b)
  a + b       →  a.__add__(b)
  x in obj    →  obj.__contains__(x)
"""


# ------------------------------------------------------------
# Without __str__ — ugly default print
# ------------------------------------------------------------
class UserNoStr:
    def __init__(self, name):
        self.name = name


user = UserNoStr("Yog")
print(user)
# something like: <__main__.UserNoStr object at 0x...>
print()


# ------------------------------------------------------------
# __str__ — friendly output for humans (used by print)
# ------------------------------------------------------------
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User(name={self.name})"


user = User("Yog")
print(user)  # User(name=Yog)
print()


# ------------------------------------------------------------
# __repr__ — for developers / lists / debugging
# ------------------------------------------------------------
# __str__  → friendly for humans
# __repr__ → detailed for developers
# In many projects people make them the same.


class UserWithRepr:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User(name='{self.name}')"


users = [UserWithRepr("Yog"), UserWithRepr("Alice")]
print(users)  # uses __repr__ inside the list
print()


# ------------------------------------------------------------
# __len__ — make len(obj) work
# ------------------------------------------------------------
class Cart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)


cart = Cart()
cart.items.append("Laptop")
cart.items.append("Mouse")

print(len(cart))  # 2  →  calls cart.__len__()
print()


# ------------------------------------------------------------
# __eq__ — make == compare by value, not memory address
# ------------------------------------------------------------
class NamedUser:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


user1 = NamedUser("Yog")
user2 = NamedUser("Yog")

print(user1 == user2)  # True  →  calls user1.__eq__(user2)
print()


# ------------------------------------------------------------
# __add__ — make + work on your objects
# ------------------------------------------------------------
class Wallet:
    def __init__(self, money):
        self.money = money

    def __add__(self, other):
        return Wallet(self.money + other.money)

    def __str__(self):
        return f"Wallet({self.money})"


wallet1 = Wallet(100)
wallet2 = Wallet(50)
wallet3 = wallet1 + wallet2  # wallet1.__add__(wallet2)

print(wallet3)  # Wallet(150)
print()


# ------------------------------------------------------------
# Real backend-ish example — readable logs
# ------------------------------------------------------------
class AccountUser:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.id})"


print(AccountUser(123, "Yog"))  # Yog (123)
print()


# ------------------------------------------------------------
# Common magic methods (don't memorize — just know they exist)
# ------------------------------------------------------------
# __init__       User()
# __str__        print(user)
# __repr__       lists, debugging
# __len__        len(obj)
# __eq__         ==
# __add__        +
# __iter__       for item in obj
# __contains__   in


# ------------------------------------------------------------
# Challenge
# ------------------------------------------------------------
# Create Library with a books list.
# Implement __str__ and __len__.
#
# library = Library([
#     "Clean Code",
#     "Design Patterns",
#     "Python Crash Course"
# ])
#
# print(library)   →  Library with 3 books
# print(len(library))  →  3
#
# Bonus: __contains__ so "Clean Code" in library → True


class Library:
    def __init__(self, books):
        self.books = books

    def __str__(self):
        return f"Library with {len(self.books)} books"

    def __len__(self):
        return len(self.books)

    def __contains__(self, book):
        return book in self.books


library = Library(
    [
        "Clean Code",
        "Design Patterns",
        "Python Crash Course",
    ]
)

print(library)
print(len(library))
print("Clean Code" in library)
