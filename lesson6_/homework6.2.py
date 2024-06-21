seconds = int(input('Enter seconds: '))
if 8640000 > seconds > 0:
    dayprint = 'дней'
    day = seconds // 86400
    hours = seconds % 86400 // 3600
    minutes = seconds % 3600 // 60
    seconds = seconds % 3600 % 60

    if day % 10 == 1 and day != 11:
        dayprint = 'день'

    elif 1 < (day % 10) < 5 and  day not in range(11,15):
        dayprint = 'дня'

    print(f'{day} {dayprint} {hours:02}:{minutes:02}:{seconds:02}')
else:
    print('too much')
