num = int(input('Введите диаметр окружности: '))
user_choice = input('Выберите что хотите узнать: площадь или периметр окружности: ')

square = (3.14 / 4) * num ** 2
perimetr = 3.14 * num

if user_choice == 'площадь':
    print('Площадь = ', square)
else:
    print('Периметр = ', perimetr)
#elif user_choice == 'периметр':
    #print('Периметр = ', perimetr)