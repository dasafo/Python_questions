# Find the sum of the series upto n terms

# Write a program to calculate the sum of series up 
# to n term. For example, if n =5 the series will 
# become 2 + 22 + 222 + 2222 + 22222 = 24690

# Method 1
n = 5
num_ini = 2
x = 0
for i in range(0, n):
    print(num_ini, end="+")
    x += num_ini
    num_ini = num_ini * 10 + 2

print("\n Sum of serie is: ", x)

# Method 2

n = 5
num_ini = 2
sum=0
a=0
for i in range(0,n):
    sum = sum*10 + num_ini
    a+=sum
print(a)
