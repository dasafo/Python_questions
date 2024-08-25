# Convert two lists into a dictionary

# Below are the two lists. Write a Python
# program to convert them into a dictionary in
# a way that item from list1 is the key and item from list2 is the value

keys = ["Pink", "Blue", "Yellow"]
values = [45, 6 ,78]

#Method 1
res = dict(zip(keys, values))
print("MEthod 1: ", res)

print()
# MEthod 2
res_dict = {}
for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})

print("MEthod 2: ", res_dict)

