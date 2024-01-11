# Remove empty strings from a list of strings

# Method 1
list1 = ["car", None, "bike", "", "plane", "", "ship", ""]

transport = []

for i in list1:
    if i:
        transport.append(i)

print("Method 1: ", transport)

print()

#Method 2

list2 = ["", "", "Apple", None, 0, "IBM", "", "Linux", "Windows"]

brands = list(filter(None, list2))
print("Method 2: ", brands)
