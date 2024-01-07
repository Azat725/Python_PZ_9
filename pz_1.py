second_passed = int(input('Введите количество секунд прошедших с начала дня: '))
user_choice = input('Выберите что хотите узнать: сколько часов, минут и секунд осталось до полуночи (или все): ')
seconds_to_midnight = 86400 - second_passed #86400 секунд в сутках
hours = seconds_to_midnight // 3600
minute = (seconds_to_midnight % 3600) // 60
seconds = (seconds_to_midnight % 3600) % 60

if user_choice == 'Все' or 'Всё' or 'все' or 'всё':
    print(f'До полуночи осталось: {hours} часов, {minute} минут и {seconds} секунд')
elif user_choice == 'Часы' or 'Часы до полуночи' or 'часы':
    print(f'До полуночи осталось: {hours} часов')
elif user_choice == 'Минуты' or 'Минуты до полуночи' or 'минуты':
    print(f'До полуночи осталось: {minute} минут')
elif user_choice == 'Секунды' or 'Секунды до полуночи' or 'секунды':
    print(f'До полуночи осталось: {seconds} секунд')
else:
    print('Error')