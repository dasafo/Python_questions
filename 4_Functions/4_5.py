#  Create an inner function to calculate the addition in the following way

#    - Create an outer function that will accept two parameters, a and b
#    - Create an inner function inside an outer function that will
#    calculate the addition of a and b
#    - At last, an outer function will add 5 into addition and return it

def out_fun(a, b):

    def inn_fun(a, b):
        return a+b
    
    add = inn_fun(a, b)
    
    return add+5

print(out_fun(5, 9))

