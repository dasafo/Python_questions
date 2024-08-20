#  Write a function called exponent(base, exp) that returns 
#  an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.
#
# Ej:
# base = 5
# exponent = 4
# 5 raises to the power of 4 is: 625 i.e. (5 *5 * 5 *5 = 625)

# Method 1
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1

    print(base, " raises to the power of ",exp , " is: ", result)

exponent(5, 4)


# Method 2
def exponent(base, exp):
    return base ** exp

base = 5
exp = 4
result = exponent(base, exp)
print(f"{base} raises to the power of {exp} is: {result}")