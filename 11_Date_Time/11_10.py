# Calculate number of days between two given dates

from datetime import datetime

date_1 = datetime(2023, 10, 21).date()
date_2 = datetime(2020, 12, 17).date()

delta = None
if date_1 > date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
else:
    print("date_2 is greater")
    delta = date_2 - date_1
print("Difference is", delta.days, "days")
