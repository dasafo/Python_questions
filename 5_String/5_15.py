#  Remove special symbols / punctuation from a string

import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation)) #3er position is for remove

print("New string is ", new_str)
