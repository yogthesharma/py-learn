# Challange 1
def greet(name):
    print(f"Hello {name}")


greet("Yog")
print()


# Challange 2
def multiply(a, b):
    return a * b


print(multiply(6, 7), end="\n")


# Challenge 3
def introduce(name, city="Gurugram"):
    print(f"Hello my name is {name} and I am from {city}")


introduce("Yog")
introduce("Twinkle", "Ahmedabad")
print()


# Bonus: 15, 25
def add(a, b=10):
    return a + b


print(add(5))
print(add(5, 20))
