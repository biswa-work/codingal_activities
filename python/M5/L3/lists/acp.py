class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def describe(self):
        print(f"Brand: {self.brand}")
        print(f"Maximum speed: {self.max_speed} km/h")


class Car(Vehicle):
    def __init__(self, brand, max_speed, model, seats):
        super().__init__(brand, max_speed)
        self.model = model
        self.seats = seats

    def describe(self):
        super().describe()
        print(f"Model: {self.model}")
        print(f"Seats: {self.seats}")

    def start(self):
        print(f"The {self.model} is ready to drive.")


car = Car("Tata", 180, "Nexon", 5)
car.describe()
car.start()
print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))
