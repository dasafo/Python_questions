# -Convert the following datetime into a string
from datetime import datetime 

given_date = datetime(2023, 10, 21)

string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)
