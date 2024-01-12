# Delete a list of keys from a dictionary


sample_dict = {
    "name": "Sofia",
    "age": 32,
    "salary": 1500,
    "city": "Berlin"}

# Keys to delete 
keys = ["name", "salary"]
for i in keys:
    sample_dict.pop(i)

print(sample_dict)

# Method 2
print()
sample_dict_2 = { j : sample_dict[j] for j in sample_dict.keys() - keys }

print(sample_dict_2)
