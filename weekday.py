# Jody Bradley
# This program tells the user whether or not today is a weekday.

import datetime
# imports datetime function

now = datetime.datetime.now()
# Defines todays date as now.

date = now.weekday()
# Defines date

day = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
# Defines weekdays as a tuple.

print('Today is', day[date])

if date < 4:
    print('Work today, zzzz')
# 0, 1, 2, 3, 4 = Monday, Tuesday, Wednesday, Thursday ,Friday, i.e. weekdays.

else:
    print('Weekend, party time!')
# Its 5 or 6 = Saturday or Sunday, i.e. the weekend!

# REFERENCES
# https://pythontic.com/datetime/date/weekday