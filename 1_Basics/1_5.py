# Write a function to return True if the first and last number 
# of a given list is same. If numbers are different then return False.

def check_numbers(arr):
    if arr[0] == arr[-1]:
        return True
    else:
        return False

print(check_numbers([44,45,76,89,44]))
