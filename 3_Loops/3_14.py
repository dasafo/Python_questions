# Reverse a given integer number

# Method 1
num = 78456
num_rever = 0

while num > 0:
    reminder = num%10
    num_rever = (num_rever*10) + reminder
    num = num // 10

print(num_rever)

# Method 2
num = 78456

num_int_str_int = int(str(num)[::-1])

print(num_int_str_int)