# Iterate a given list and check if a given element
# exists as a key’s value in a dictionary. If not, delete it from the list

list1 = [34, 67, 36, 12, 98, 54, 72, 44]
dict_sample = {'Lukas':56, 'Emma':54, 'Sofia': 34, 'Kevin':78, "Manuel": 98}

list1[:] = [i for i in list1 if i in dict_sample.values()]
print(list1)

