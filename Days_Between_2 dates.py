# find number of days between two days
from datetime import date
f_date = date(1996, 10, 29)
l_date = date(2020, 10, 29)
delta = l_date - f_date
print(delta.days)