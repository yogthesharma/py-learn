"""
Polymorphism

Different classes share an interface (e.g. `.area()`) but implement it
their own way. Callers work with the base type or any subclass.

Loop over a mixed list and call the same method — each object runs its
version (Rectangle vs Circle).

Use when behavior varies by type but call sites should stay simple
(shapes, payment processors, serializers).

Gotcha: base methods that `pass` or raise are placeholders — subclasses
must override or callers get useless results.
"""

import math


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


shapes = [
    Rectangle(10, 20),
    Circle(5),
]

for shape in shapes:
    print(shape.area())
