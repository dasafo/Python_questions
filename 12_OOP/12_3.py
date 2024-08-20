# Create a child class Bus that will inherit all of
# the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus1 = Bus("Fiat", 100, 35)
print("Name: ", bus1.name)
print("Max_Speed: ", bus1.max_speed)
print("mileage: ", bus1.mileage)
