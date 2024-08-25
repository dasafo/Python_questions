# Return multiple values from a function

# Write a program to create function calculation()
# such that it can accept two variables and calculate
# addition and subtraction. Also, it must return both
# addition and subtraction in a single return call.

# Method 1
def calculation(a, b):
    sum = a+b
    res = a-b
    return sum, res

result = calculation(34, 23)
print(result)

print()

# Method 2
def calculation2(a, b):
    return a+b, a-b

add, sub = calculation2(89, 45)
print(add, sub)
