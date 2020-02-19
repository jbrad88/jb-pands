import datetime

now = datetime.datetime.now()

date = now.weekday()
day = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}

print('Today is', day[date])

if date < 4:
    print('Work today, zzzz')
else:
    print('Weekend, party time!')

