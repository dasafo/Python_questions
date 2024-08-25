# Print a downward Half-Pyramid Pattern of Star (asterisk)
#
# * * * * *  
# * * * *  
# * * *  
# * *  
# * 

# Method 1
for i in range(6, 0, -1):
    
    for j in range(0, i-1):
        
        print("*", end = " ")

    print(" ")


# Method 2
n =5

for i in range(n, 0, -1):
    print('*' * i)