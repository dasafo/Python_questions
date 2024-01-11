# Turn every item of a list into its square

# Given a list of numbers. write a program
# to turn every item of a list into its square.

list1 = [9, 6, 11, 33, 4, 7]
list_squeare = []

for i in list1:
    list_squeare.append(i*i)

print(list_squeare)

# Method2

list_squeare_2 =[ j*j for j in list1]
print("MEtho2: ", list_squeare_2)
