# Count the occurrence of each element from a list

# Write a program to iterate a given list and count
# the occurrence of each element and create a dictionary
# to show the count of each element.

list = [34, 4, 34, 56, 4, 11, 11, 6, 4, 8, 0,9, 6]

dic_list = {}

for i in list:
    if i in dic_list:
        dic_list[i] +=1
    else:
        dic_list[i] = 1

print(dic_list)
