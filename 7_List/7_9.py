
# Replace list’s item with new value if found

# You have given a Python list. Write a program
# to find value 20 in the list, and if it is present,
# replace it with 200. Only update the first occurrence of an item.

list1 = [45, 6, 78, 20, 23, 9, 20, 80]

ind = list1.index(20)

list1[ind]=200

print(list1)
