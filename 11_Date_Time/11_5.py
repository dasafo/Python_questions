# Find the day of the week of a given date

from datetime import datetime 

given_date = datetime(2023, 10, 21)

print(given_date.strftime('%A'))
