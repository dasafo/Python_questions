# Print list in reverse order using a loop

list = [1, 4, 65, 2, 89, 8] # 6 int

# Method 1
list_rev = reversed(list)

for i in list_rev:
    print(i, end=" ")

print()

# Method 2
for i in range(len(list)-1, -1, -1): # from position 5(len(list)-1) to 0(-1)
    print(list[i], end=" ")
