# Convert the following JSON into Vehicle Object

# {"name" : "Toyota", "engine" : "4.5L", "price" : 45000}

import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def VehicleDecoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])

vehicle_json = json.loads('{"name" : "Toyota", "engine" : "4.5L", "price" : 45000}', object_hook=VehicleDecoder)

print(vehicle_json.name, vehicle_json.engine, vehicle_json.price)
