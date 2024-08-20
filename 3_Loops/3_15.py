# Use a loop to display elements from a given 
# list present at odd index positions

list1 = [45, 6, 43, 2, 89, 76, 22]

# Method 1
for i in range(0, len(list1)):
    if i % 2 !=0:
        print(list1[i], end=" ")

print()

# Method 2
for i in list1[1::2]:
    print(i, end=" ")
