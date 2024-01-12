# Create a dictionary by extracting the keys from a given dictionary

# Write a Python program to create a new dictionary by extracting
# the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Sofia",
    "age": 32,
    "salary": 1500,
    "city": "Berlin"}

# Keys to extract
keys = ["name", "salary"]

# Method 1
dict_extrac = {}

for i in sample_dict.keys():
    if i in keys:
        dict_extrac.update({i:sample_dict[i]})

print("MEthod 1: ",dict_extrac)

print()

#MEthod 2

dict_extrac_2= { j:sample_dict[j] for j in keys }
print("MEthod 2: ", dict_extrac_2)
