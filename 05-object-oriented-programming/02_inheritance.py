"""
Inheritance

Subclass extends a parent: `class Car(Vehicle)`. Child gets parent methods
and can override them (`start`) or add new ones (`honk`).

`super().__init__(...)` runs the parent's constructor before setting
child-specific attributes.

Use when types share behavior but differ in details (Vehicle → Car,
Shape → Rectangle).

Gotcha: overriding replaces the parent method entirely — call `super()`
when you still need parent setup or behavior.
"""

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print("Vehicle Started")

    def stop(self):
        self.speed = 0
        print("Vehicle Stopped")


class Car(Vehicle):
    def __init__(self, brand, speed, color):
        super().__init__(brand, speed)
        self.color = color

    def honk(self):
        print(f"{self.brand} is honking")

    def start(self):
        print(f"{self.brand} Started")


car = Car("BMW", 0, "Black")

car.start()
car.honk()
car.stop()
