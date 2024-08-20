# Initialize dictionary with default values

# In Python, we can initialize the keys with the same values.

car = ["BMV", "Fiat"]
features = {"Wheels" : "red", "seat":"black", "boots":2}

features = dict.fromkeys(car, features)
print(features)
