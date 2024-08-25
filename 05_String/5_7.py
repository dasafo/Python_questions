# String characters balance Test

# Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all the
# characters in the s1 are present in s2. The
# character’s position doesn’t matter.

# Case 1:
# 
# s1 = "Yn"
# s2 = "PYnative"
# 
# Expected Output: True

# Case 2:
# 
# s1 = "Ynf"
# s2 = "PYnative"
# 
# Expected Output: False

# MEthod 1
def balanced(s1, s2):
    count = 0
    for i in s1:
        if i in s2:
            count += 1
        else:
            count = 0
    if count == len(s1):
        return True
    else: return False

print("Method 1: ", balanced("krpa", "mariposa"))

print()
# Method 2
def balanced2(s1, s2):
    bol = True

    for i in s1:
        if i in s2:
            bol = True
        else:
            bol = False
    return bol

print("MEthod 2: ", balanced2("dpns", "headphones"))
