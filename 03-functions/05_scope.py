# Challenge 1

name = "Yog"


def greet():
    name = "Alice"
    print(name)


greet()

print(name)

# Output: Alice, Yog


# Challenge 2
def test():
    value = 10


test()

print(value)

# Will this work no value is outta scope


# Challenge 3
count = 0


def increment(count):
    count += 1


count = increment(count)

print(count)

# Challenge 4
x = 100


def outer():
    x = 50

    def inner():
        print(x)

    inner()


outer()
# output 50

# Interview question
# I dont know may be because we can read it but can't mutate
