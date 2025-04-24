# ------------- Math Date Time Calender ----------------

# _____________ 1. Math Module – for mathematical operations
# This module helps you do advanced math tasks like square root, power, pi, sin/cos etc.
import math

print(math.sqrt(16))        # Square root → 4.0
print(math.pow(2, 3))       # Power (2^3) → 8.0
print(math.pi)              # Pi value → 3.14159...
print(math.ceil(4.3))       # Round up → 5
print(math.floor(4.7))      # Round down → 4


# ______________ 2. datetime Module – for working with date and time ___________________ 
# datetime Module – for working with date and time
# This module helps you get current date/time, make date objects, calculate days, etc.
import datetime

now = datetime.datetime.now()           # Current date & time
print("Current date & time:", now)

today = datetime.date.today()           # Only date
print("Today date:", today)

birthday = datetime.date(2001, 7, 4)    # Custome date
print("Birth date:", birthday)

# ______________ 3. calendar Module – To Work with Calendars _________________
# This module lets you print the full calendar of a month or year, and also check weekdays or day names.
import calendar

print(calendar.month(2025, 4))           # April 2025 calendar

# Print the names of weekdays (Monday to Sunday)
weekdays = list(calendar.day_name)

print("Days of the week:")
for day in weekdays:
    print(day)

