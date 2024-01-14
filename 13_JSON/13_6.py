# Convert the followong Vehicle Object into JSON

import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

vehicle = Vehicle("Tesla", "4.5L", 40000)
vehicle_json = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(vehicle_json)

