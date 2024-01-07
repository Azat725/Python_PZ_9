cost = float(input('Введите стоимость одной приставки: '))
quantity = float(input('Введите количество приставок: '))
discount = float(input('Введите процент скидки: '))
user_choice = input('Если вы хотите узнать общую сумму заказа напишите "Общая стоимость", если вы хотите узнать стоимость одной приставки наипшите "Одна приставка" ')
final_cost_with_discount = cost - (cost * (discount / 100)) #выводит стоимость одной приставки со скидкой
total_cost =  cost * quantity 
total_cost_with_discount = total_cost - (total_cost * (discount / 100))

if user_choice == 'Одна приставка':
    print(int(final_cost_with_discount))
elif user_choice == 'Общая стоимость':
    print(int(total_cost_with_discount))
elif discount == 0:
    print(int(total_cost))
elif discount <= -1:
    print('Ошибка, скидка не может быть отрицательна!!!')