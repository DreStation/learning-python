# Get user input
# Ask for a weekday
# Ask for a month
# Ask for a year
# Print the number of occurences of the weekday in that month and year

import calendar

while True:
    try:
        print("Which day of the week do you want to count?")
        print("0 = Monday\n1 = Tuesday\n2 = Wednesday\n3 = Thursday\n4 = Friday\n5 = Saturday\n6 = Sunday\n7 = Exit")
        weekday = int(input("Enter a number: "))
        if weekday == 7:
            break

        month = int(input("Enter a month: "))
        year = int(input("Enter a year: "))
    except ValueError:
        print("That's not a number!")
        continue

    count = 0
    # Loop thru a list of weeks in a month
    for week in calendar.monthcalendar(year, month):
        if week[weekday] != 0: # If weekday is not 0, it means it's in that week
            count += 1
    print("There are " + str(count) + " " + calendar.day_name[weekday] + "s in " + calendar.month_name[month] + " " + str(year))
