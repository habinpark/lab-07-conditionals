import datetime

now = datetime.datetime.now()
#print(now.year,now.month,now.day,now.hour,now.minute,now.second)
Time = now.hour
if Time <= 5:
    print("It's early. You should be sleeping!")
elif Time <= 7:
    print('Wake up, brew that coffee, get that mile run in, and get that breakfast…')
elif Time <= 9:
    print('Time to go to work.')
elif Time <= 12:
    print('You should be working!')
elif Time <= 13:
    print('Take your lunch break!')
elif Time <= 17:
    print('Do you feel that afternoon lull?')
elif Time <= 19:
    print('Time to hit the gym…')
elif Time <= 21:
    print('Gotta eat that dinner.')
elif Time <= 23:
    print('Get that SLEEP. And rePEAT!')
else:
    print("You didn’t type an acceptable value! (0-23)")
