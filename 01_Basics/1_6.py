# Iterate the given list of numbers and print only those 
# numbers which are divisible by 5

arr = [23, 12, 50, 3, 45, 30, 33]
for i in range(0, len(arr)-1):
    if arr[i]%5 == 0:
        print(arr[i])
