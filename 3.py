# Given an array , find if the number exists
# This is a `recursive` implementation of the
# binary search. If the element is not found
# it returns -1
#
#
# lst = array
# key = number to search
# l = from what number the search starts.
# r = external position of the search

def binarySearch(lst, key, l, r):
    if r >= l:
        mid = l + (r - l) // 2
        # use print(l, mid, r) to view the process
        print(l,mid,r)
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            return binarySearch(lst, key, mid + 1, r)
        elif lst[mid] > key:
            return binarySearch(lst, key, l, mid - 1)
    else:
        return -1


arr = [int(i) for i in range(101)]
print(arr)
print(binarySearch(arr, 8, 0, len(arr) - 1))
