# Write a program to extract each digit from an integer
# in the reverse order.

num = 18756

while num > 0:
    digit = num % 10
    num = num // 10
    
    print(digit, end = " ")
