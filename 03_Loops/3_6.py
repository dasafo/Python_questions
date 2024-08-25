# Count the total number of digits in a number

# Write a program to count the total number of digits 
# in a number using a while loop. For example, the 
# number is 75869, so the output should be 5.

# Method 1
num = 6874913

count = 0

while num != 0:
    count +=1
    num = num //10
print(count)


# Method 2
num = 6874913

num_str = str(num)

print(len(num_str))
