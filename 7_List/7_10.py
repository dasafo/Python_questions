# Remove all occurrences of a specific item from a list.

# Given a Python list, write a program to remove
# all occurrences of item 20.


list1 = [45, 6, 78, 20, 23, 9, 20, 80]

def del_occurrences(list1, num):
    return [i for i in list1 if i != num]

print(del_occurrences(list1, 20))
