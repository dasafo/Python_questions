# Calculate the sum of all numbers from 1 to a given number

# Write a program to accept a number from a user and 
# calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10 the output should 
# be 55 (1+2+3+4+5+6+7+8+9+10)

# Method 1
def number():
    num = int(input('Enter a number(int): '))
    multip = 0
    for i in range(1, num+1):
        multip += i
    return print(multip) 

number()

# Method 2
n = int(input("Enter a number(int): "))

summ = sum(range(1, n+1))

print ('Sum is: ', summ)
