#Iterate both lists simultaneously

# Given a two Python list. Write a program
# to iterate both lists simultaneously and display
# items from list1 in original order and items
# from list2 in reverse order.

list1 = [23, 43, 56, 78, 90]
list2 = [3, 5, 6, 7, 8]

for i, j in zip(list1, list2[::-1]):
    print(i, j)
