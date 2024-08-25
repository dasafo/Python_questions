# Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# Method 1
for num in range(10):
    
    for i in range(num):
    
        print(num, end=" ")
    
    print("\n")


# Method 2

for i in range(1,6):
    print((str(i)+ ' ') *i)