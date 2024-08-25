# Given two list of numbers, write a program to create a new list
# such that the new list should contain odd numbers form the first
# list and even numbers from the second list.

def merg_odd_even_lists(list1, list2):
    merg_list = []
    
    for i in list1:
        if i % 2 != 0:
            merg_list.append(i)
    
    for i in list2:
        if i % 2 == 0:
            merg_list.append(i)

    return merg_list 

print(merg_odd_even_lists([2, 4, 6, 13, 45, 60], [34, 43, 12, 17, 66, 88]))
