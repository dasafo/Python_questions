#  Find words with both alphabets and numbers

# Write a program to find words with both alphabets
# and numbers from an input string.

str = "User David85 is playing against player Nauka17."
res=[]
temp = str.split()

for i in temp:
    if any(char.isalpha() for char in i) and any(di.isdigit() for di in i):
        res.append(i)

print(res)
