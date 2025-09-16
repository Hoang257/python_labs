minutes = int(input('Минуты: '))
hour = minutes//60
min = minutes % 60
if min < 10: 
    min = '0' + f'{min}'
print(f'{hour}:{min}')