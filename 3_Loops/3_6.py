# Count the total number of digits in a number

# Write a program to count the total number of digits 
# in a number using a while loop. For example, the 
# number is 75869, so the output should be 5.

num = 6874913

count = 0

while num != 0:
    count +=1
    num = num //10
print(count)
