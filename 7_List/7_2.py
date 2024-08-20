# Concatenate two lists index-wise

# Write a program to add two lists index-wise. Create a new
# list that contains the 0th index item from both the list,
# then the 1st index item, and so on till the last element.
# any leftover items will get added at the end of the new list.

list1 = ["Th", "re", "thi", "i", "incre"]
list2 = ["e", "al", "ng", "s", "dible"]

list3 = [i + j for i,j in zip(list1, list2)]
print(list3)
