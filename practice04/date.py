#1
from datetime import date, timedelta

today = date.today()
new_date = today - timedelta(days=5)

print(new_date)

#2
from datetime import date, timedelta

today = date.today()

print("Yesterday:", today - timedelta(days=1))
print("Today:", today)
print("Tomorrow:", today + timedelta(days=1))

#3
from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print(no_microseconds)

#4
from datetime import datetime

date1 = datetime(2024, 1, 1, 10, 0, 0)
date2 = datetime(2024, 1, 1, 12, 0, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print(seconds)