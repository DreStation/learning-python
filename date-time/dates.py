from datetime import date
from datetime import time
from datetime import datetime

# Get today's date
today = date.today()
print("Today's date is", today)

print("Date components:", today.day, today.month, today.year)

# Get the day of the week (0=Monday, 6=Sunday)
print("Today's weekday # is:", today.weekday())

# Get the date and time
today = datetime.now()
print("The current date and time is", today)

# Get just the time
t = datetime.time(datetime.now())
print("The current time is", t)