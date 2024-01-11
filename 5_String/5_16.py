# Removal all characters from a string except integers

str = "We are too young. Im 18 and my friend 20."

str_digits = "".join([i for i in str if i.isdigit()])

print(str_digits)
