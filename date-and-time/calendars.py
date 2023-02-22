import calendar

# Print a plain text monthly calendar for February 2023
c = calendar.TextCalendar(calendar.SUNDAY) # Set Sunday as 1st day
str = c.formatmonth(2023, 2, 0, 0)
print(str)

# HTML calendar -> prints an HTML table
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# str = hc.formatmonth(2023, 2)
# print(str)

# Loop thru calendar
for i in c.itermonthdays(2023, 2):
    print(i)

# Print every month name
for name in calendar.month_name:
    print(name)

# Print every day name
for day in calendar.day_name:
    print(day)

# Calculate days based on a rule: For example, consider a team meeting on
# the first Friday of every month. To figure out what days that would be
# for each month, we can use this script:
print("Team meetings will be on:")

# Loop thru each month
for m in range(1, 13):
    cal = calendar.monthcalendar(2023, m)

    # Figure out if 1st Friday is on 1st or 2nd week
    week1 = cal[0]
    week2 = cal[1]
    if week1[calendar.FRIDAY] != 0:
        meetday = week1[calendar.FRIDAY]
    else:
        meetday = week2[calendar.FRIDAY]

    print(calendar.month_name[m], meetday)