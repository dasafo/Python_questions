# Convert string into a datetime object

# For example, You received the following date
# in string format. Please convert it into Python’s DateTime object.

from datetime import datetime

date_string = "Dec 15 2023  7:45AM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)
