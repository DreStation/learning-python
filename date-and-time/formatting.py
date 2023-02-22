from datetime import datetime

now = datetime.now()

print(now.strftime("The current year is: %Y\n"))

print(now.strftime("%a, %d, %b, %y"))
print(now.strftime("%A, %D, %B, %Y\n"))

print(now.strftime("Local date and time: %c"))
print(now.strftime("Local date: %x"))
print(now.strftime("Local time: %X\n"))

print(now.strftime("12hr time: %I:%M:%S %p"))
print(now.strftime("24hr time: %H:%M"))