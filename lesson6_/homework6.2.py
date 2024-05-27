seconds = int(input('Enter seconds: '))


dayprint = 'дней'
day = seconds // 86400
hours = seconds % 86400 // 3600
minutes = seconds % 3600 // 60
seconds = seconds % 3600 % 60
if day == 1:
    dayprint = 'день'
elif day > 1 and day < 5:
    dayprint = 'дня'



print(f'{day} {dayprint} {hours:02}:{minutes:02}:{seconds:02}')