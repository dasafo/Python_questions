# Create a mixed String using the following rules

# Given two strings, s1 and s2. Write a program to
# create a new string s3 made of the first char of s1,
# then the last char of s2, Next, the second char of s1
# and second last char of s2, and so on. Any leftover
# chars go at the end of the result.


def fun(s1, s2):
    for i in range(0, len(s1)):
        j = -1 + i
        print(s1[i] + s2[j])
fun("table", "windows")
