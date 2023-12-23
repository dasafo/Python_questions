# Given two integer numbers, return their product only if the product 
# is equal to or lower than 1000. Otherwise, return their sum.

def product (a, b):
    if a*b <= 1000:
        return a*b
    else:
        return a+b

print(product(1000,1000))
