# Find the factorial of a given number

# Write a program to use the loop to find 
# the factorial of a given number. The factorial (symbol: !) 
# means to multiply all whole numbers from the chosen number down to 1.

factorial = 1
num = 5
for i in range(1, num+1):
    factorial = factorial *i
print(factorial)
