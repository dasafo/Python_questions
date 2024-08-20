# Rename key of a dictionary

# Write a program to rename a key city to a location
# in the following dictionary.

sample_dict = {
    "name": "Sofia",
    "age": 32,
    "salary": 1500,
    "city": "Berlin"}

sample_dict['location'] = sample_dict.pop('city')

print(sample_dict)
