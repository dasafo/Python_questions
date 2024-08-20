#  Add a week (7 days) and 12 hours to a given date


from datetime import datetime, timedelta 

given_date = datetime(2023, 10, 21)

res_date = given_date + timedelta(days=7, hours=12)
print(res_date)
