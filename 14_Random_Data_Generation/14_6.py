# Generate a random Password which meets the following conditions

#    - Password length must be 10 characters long.
#    - It must contain at least 2 upper case letters,
#    1 digit, and 1 special symbol.

import random
import string

def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation 
    # 1. 6 random characters
    password = random.sample(randomSource, 6)

    # 2. Two upper case letters
    password += random.sample(string.ascii_uppercase, 2)

    # 3. One digit
    password += random.choice(string.digits)

    # 4. One special symbol
    password += random.choice(string.punctuation)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

print(randomPassword())
