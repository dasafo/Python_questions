# Accept a list of 5 float numbers as an input from the user

list = []

for i in range(0,5):
    print("Enter number at position ", i,":")
    x = float(input())
    list.append(x)

print(f"The list of numbers is: {list}")
