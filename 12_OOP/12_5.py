# Define a property that must have the same value
# for every class instance (object)

# Define a class attribute”color” with a default
# value white. I.e., Every Vehicle should be white.

# Use the following code for this exercise.


class Vehicle:

    color = "black"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus1 = Bus(name = "VW", max_speed = 120, mileage = 35)
car1 = Car(name = "Renault", max_speed = 240, mileage = 45)
print("Bus color: ", bus1.color)
print("Bus name: ",bus1.name)
print()
print("Car color: ", car1.color)
print("Car name: ", car1.name)


