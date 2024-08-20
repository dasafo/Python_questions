# Generate random String of length 5

# Note: String must be the combination of the UPPER case
# and lower case letters only. No numbers and a special symbol.

import random
import string

def randomString(str_lenght):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(str_lenght))

print(randomString(5))
