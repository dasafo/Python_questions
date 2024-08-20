# Given two integer numbers, return their product only if the product 
# is equal to or lower than 1000. Otherwise, return their sum.

# Method 1
def product (a, b):
    if a*b <= 1000:
        return a*b
    else:
        return a+b

print(product(1000,1000))


# Method 2
def product(a, b):
    return a*b if a*b <=1000 else a+b

print(product(10, 2))