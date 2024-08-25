# Get all values from the dictionary and add them
# to a list but don’t add duplicates


dict_sample = {'Lukas':56, 'Emma':54, 'Sofia': 34, 'Kevin':78, "Manuel": 98, "Ana":54, "Luis":34}

list1 = list()

for i in dict_sample.values():
    if i not in list1:
        list1.append(i)

print(type(list1))
