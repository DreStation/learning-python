import datetime
from datetime import timedelta

# Timedelta is a duration of time or a time span

print(timedelta(days = 365, hours = 5, minutes = 1))

# Today + 365 days = 1 year from now
now = datetime.datetime.now()
print("One year from now it will be: " + str(now + timedelta(days = 365)))

# Multi arg timedelta
print("In 2 days and 3 weeks, it will be: " + str(now + timedelta(days = 2, weeks = 3)))

# Subtract time
t = datetime.datetime.now() - timedelta(weeks = 1)
print("One week ago was " + str(t.strftime("%A %B %d, %Y")))



# How many days until April Fools Day?
today = datetime.date.today()
afd = datetime.date(today.year, 4, 1)

# Compare the dates
if afd < today:
    print("April Fools Day already went by %d days ago", ((today-afd).days))
    afd = afd.replace(year = today.year + 1) # Date is passed, set afd to next year

# Now calculate the amount of time until April Fools Day
time_to_afd = afd - today
print("It's just", time_to_afd.days, "days until April Fools Day!")