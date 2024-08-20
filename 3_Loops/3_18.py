# Write a program to print the following start pattern using the for loop

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range(1,6):
    print('*' * i, end=" ")
    print()
for i in range(6, 0, -1):
    print('*' * i, end=" ")
    print()


