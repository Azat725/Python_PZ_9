hours = int(input('Введите количество часов: '))

if 0 <= hours < 6:
    print('Good Night')
elif 6 <= hours < 13:
    print('Good Morning')
elif 13 <= hours < 17:
    print('Good Day')
elif 17 <= hours < 24 or hours == 0:
    print('Good Evening')
else:
    print('Некорректный ввод времени')