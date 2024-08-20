# Subtract a week (7 days)  from a given date in Python

from datetime import datetime, timedelta

given_date = datetime(2023, 10, 21)
print(given_date)

res_date = given_date - timedelta(days=7)
print("Date minus 7 days: ",res_date)

