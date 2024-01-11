# Calculate the sum and average of the digits present in a string

# Given a string s1, write a program to return the sum and average
# of the digits that appear in the string, ignoring all other characters.

# Given: str1 = "PYnative29@#8496"
# 
# Expected Outcome: Sum is: 38 Average is  6.333333333333333

str1 = "mala34cat87@#i9?12"
sum = 0
count = 0
for i in str1:
    if i.isdigit():
        sum = sum + int(i)
        count +=1
avg = sum / count

print("Sum = ", sum, "\n", "Average = ", format(avg, ".2f"))

