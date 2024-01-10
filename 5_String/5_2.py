# Append new string in the middle of a given string

# Given two strings, s1 and s2. Write a program to
# create a new string s3 by appending s2 in the middle of s1.

def fun(s1, s2):
    m1 = int(len(s1) / 2)
    m1_ini = s1[0:m1]
    m1_fin = s1[m1::]

    print(m1_ini + s2 + m1_fin)

fun("Anana", "Apple")
