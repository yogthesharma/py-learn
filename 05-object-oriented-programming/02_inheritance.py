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
