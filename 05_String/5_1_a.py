#  Create a string made of the first, middle and last character

# Write a program to create a new string made of an input 
# string’s first, middle, and last character.

string = "david"

first_string = string[0]

middle_position = int(len(string) / 2)
middle_string = string[middle_position]

last_string = string[-1]

res = first_string + middle_string + last_string

print(res)
