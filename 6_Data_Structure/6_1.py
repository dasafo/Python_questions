# Create a list by picking an odd-index items from the
# first list and even index items from the second

# Given two lists, l1 and l2, write a program to create
# a third list l3 by picking an odd-index element from
# the list l1 and even index elements from the list l2.

l1 = [4, 5, 6, 7, 45, 23, 12]
l2 = [9, 76, 45, 6, 34, 23, 122, 8]

l3 = list()

odd_list = l1[1::2]
even_list = l2[0::2]

l3.extend(odd_list)
l3.extend(even_list)
print(l3)

