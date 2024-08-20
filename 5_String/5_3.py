# Create a new string made of the first, middle, and last
# characters of each input string

# Given two strings, s1 and s2, write a program to return
# a new string made of s1 and s2’s first, middle, and last characters.

def fun(s1, s2):
    first_letters = s1[0] +  s2[0]
    middle_letters = s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
    last_letters = s1[-1] + s2 [-1]

    print(first_letters + middle_letters + last_letters)

fun("Tormentoso", "Claudicaron")
