# Generate 3 random integers between 100 and 999 which is divisible by 5

# Reference article for help: Python get a random number within a range

import random

for i in range(3):
    print(random.randrange(100, 900, 5), end=", ")
