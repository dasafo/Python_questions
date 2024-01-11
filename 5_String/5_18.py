# Replace each special symbol with # in the following string

str1 = "Pau is a engineer &  football player? /*Incredible!%"

import string

for i in string.punctuation:
    str1 = str1.replace(i, "")

print(str1)
