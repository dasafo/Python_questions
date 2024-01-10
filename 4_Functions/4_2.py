# Create a function with variable length of arguments

# Write a program to create function func1() to accept
# a variable length of arguments and print their value.

# Note: Create a function in such a way that we can pass
# any number of arguments to this function, and the function
# should process them and display each argument’s value.

def fun(*args):
    for i in args:
        print(i, end=" ")
    print("\n")

fun(29, 23, "Juan")
fun("David", 4, 2, 24, 6, "Elvira")
