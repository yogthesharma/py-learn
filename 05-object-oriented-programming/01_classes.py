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
