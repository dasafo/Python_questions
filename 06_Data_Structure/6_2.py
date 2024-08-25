# Remove and add item in a list

# Write a program to remove the item present at
# index 4 and add it to the 2nd position and at the end of the list.

list1 = [87, 45, 6, 29, 98, 13, 12]
print("Original list: ", list1, end="\n")

num = list1.pop(4)
print("List without index 4: ", list1, end="\n")

list1.insert(2, num)
list1.append(num)
print("List with number ",num," add in index 2: ",list1, end="\n")
print("List with number ", num, "add at the end of the list: ", list1)
