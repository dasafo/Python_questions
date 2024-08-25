# Display numbers from a list using loop

# Write a program to display only those numbers
# from a list that satisfy the following conditions

#    - The number must be divisible by five
#    - If the number is greater than 150, then skip it 
#    and move to the next number
#    - If the number is greater than 500, then stop the loop

list = [4, 60, 347, 120, 560, 44, 15, 890]

for i in list:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i%5 == 0:
        print(i)
