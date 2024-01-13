# Create a Bus child class that inhertis form the Vehicle class.
# The default fare charge of any cehicle is seating capacity*100
# If Vehicle is Bus instance, we need to add an extra 10% on full
# fare as a maintenance charge. So total fare for bus instance will
# become the final ampount = total fare + 10% of the total fare.

# Note: The bus seating capacity is 50. So the final amount fare
# anount shoud be 5500. You nedd to override the fare() 
# method of a Vehicle class in Bus class.

# Use the following code for your parent Vehicle class. We need
# to access the parent class from inside a metdho of a child class


class Vehicle:
    def __init__(self, name, capacity, mileage):
        self.name = name
        self.capacity = capacity
        self.mileage = mileage
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is: ", School_bus.fare())
