import datetime
# imports datetime function

now = datetime.datetime.now()
# Defines todays date as now.

date = now.weekday()
# Defines date

day = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
# Sets dictionary for date names in relation to indexing used by datetime.

print('Today is', day[date])

if date < 4:
    print('Work today, zzzz')
# 0, 1, 2, 3, 4 = Monday, Tuesday, Wednesday, Thursday ,Friday, i.e. weekdays.

else:
    print('Weekend, party time!')
# Its 5 or 6 = Saturday or Sunday, i.e. the weekend! 
