#  Create an inner function to calculate the addition in the following way

#    - Create an outer function that will accept two parameters, a and b
#    - Create an inner function inside an outer function that will
#    calculate the addition of a and b
#    - At last, an outer function will add 5 into addition and return it

# Method 1
def out_fun(a,b):
    
    def inn_fun():
        return a+b
    
    return inn_fun() + 5

print(out_fun(3,3))