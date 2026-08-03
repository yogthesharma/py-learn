"""
Classes

A class defines data (attributes) and behavior (methods). `__init__` runs
on construction; `self` refers to the instance being built.

Methods take `self` as the first parameter. State lives on `self.attr`.

Use classes when multiple values and operations belong together (a Car
with brand, speed, start/stop/accelerate).

Gotcha: forgetting `self.` creates a local variable, not an instance
attribute — the object won't remember it.
"""

class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed

    def start(self):
        print(f"{self.brand} started.")

    def stop(self):
        self.speed = 0
        print(f"{self.brand} stopped.")

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} accelerated to {self.speed}km/h.")


car = Car("BMW", "Black", 0)

car.start()
car.accelerate(40)
car.accelerate(30)
car.stop()
