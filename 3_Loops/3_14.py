# Reverse a given integer number

num = 78456
num_rever = 0

while num > 0:
    reminder = num%10
    num_rever = (num_rever*10) + reminder
    num = num // 10

print(num_rever)
