# Determine if bus1 is also an isntance of the Vehicle class


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus1 = Bus("Fiat", 100, 56)

print(isinstance(bus1, Vehicle))
