file_size_gb = float(input('Введите размер файла в гигабайтах: ')) #пользователь вводит размер в гигабайтах
internet_speed_mbps = float(input('Введите скорость интернета в мегабит в секунду: ')) #пользователь вводит скорость в битах в секунду
choice = str(input('Выберите вариант подсчета часы/минуты/секунды: '))

internet_speed_bps = internet_speed_mbps * 1000000 / 8
time_seconds = (file_size_gb * 8 * 1000000000) / internet_speed_bps

if choice.lower() == 'часы':
    time_hour = time_seconds / 3600
    print(f'Файл загрузиться за {time_hour:.1f} часов')
elif choice.lower() == 'минуты':
    time_minute = time_seconds / 60
    print(f'Файл загрузиться за {time_minute:.1f} минут')
elif choice.lower() == 'секунды':
    print(f'Файл загрузиться за {time_seconds:1f} секунд')
else:
    print('Выбор времени некорректен')