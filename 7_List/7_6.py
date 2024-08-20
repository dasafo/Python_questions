# Remove empty strings from the list of strings

list1 = ["car", "", "plane", "skate","", "bus"]

list_clean = filter(None, list1)

print(list(list_clean))
