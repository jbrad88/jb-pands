import datetime

today = datetime.datetime.now()

#extract today index
day = today.weekday()

#print(day) testing only

#created dict for day names
dayname ={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

print("Today is ... ", dayname[day])

#print next line based on day index extracted

if day <= 4:
    print("boo its a weekday no fun")
else:
    print("yes its the weekend")