# Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to
# create a new string s3 made of the first char of s1,
# then the last chr of s2, Next, the second char of s1
# and second last char of s2, and so on. Any leftover
# chars go at the end of the result.

str1 = "longer"
str2 = "butterfly"

leng1 = len(str1)
leng2 = len(str2)

lenght = leng1 if leng1 > leng2 else leng2

result = ""
str2 = str2[::-1]
st = []
for i in range(lenght):
    if i < leng1:
        result += str1[i]
    if i < leng2:
        result += str2[i]

print(result)
