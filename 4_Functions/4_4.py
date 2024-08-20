# Create a function with a default argument

# Write a program to create a function show_employee()
# using the following conditions.

#    - It should accept the employee’s name and salary and
#    display both.
#    - If the salary is missing in the function call then
#    assign default value 9000 to salary

def show_employee(name, salary=9000):
    return print("Name: ", name, ". Salary: ", salary)

show_employee("David")
show_employee("Paula", 890)
