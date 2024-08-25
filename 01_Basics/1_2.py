# Write a program to iterate the first 10 numbers, and in 
# each iteration, print the sum of the current and previous number.


def numbers(arr):
    for i in range(1, len(arr)):
        print(arr[i-1] + arr[i])

print(numbers([1, 2, 3, 4, 5, 6]))
