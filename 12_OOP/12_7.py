# Check type of an object
# Write a program to determine which class a give
# Bus object belongs to.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus1 = Bus("Fiat", 100, 56)

print(type(bus1))
