#  Check if a value exists in a dictionary

# We know how to check if the key exists in a dictionary.
# Sometimes it is required to check if the given value is present.

# Write a Python program to check -if value 200 exists
# in the following dictionary.

dict1 = {'blue' : 150, 'brown' : 200, 'black' : 4, 'orange' : 70}

if 200 in dict1.values():
    print ('200 exits into the dictionary')
