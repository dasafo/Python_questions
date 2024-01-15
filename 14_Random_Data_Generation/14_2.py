# Random Lottery Pick. Generate 100 random lottery tickets and pick
# two lucky tickets from it as a winner.

# Note you must adhere to the following conditions:

#    - The lottery number must be 10 digits long.
#    - All 100 ticket number must be unique.

# Hint: Generate a random list of 1000 numbers using randrange()
# and then use the sample() method to pick lucky 2 tickets.

import random

tickets_list = []

for i in range(100):
    #our numbers of the list must be 10 digits long
    tickets_list.append(random.randrange(1000000000, 9999999999))

winners = random.sample(tickets_list, 2)
print(winners, sep=", ")
