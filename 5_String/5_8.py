# Find all occurrences of a substring in a given string by ignoring the case

# Write a program to find all occurrences of “USA” in a given string
# ignoring the case. 

str = "Nobody wants to live in USA. What usa about?"

str_s = "USA"

str_low = str.lower()

counter = str_low.count(str_s.lower())

print("USA times: ", counter)
