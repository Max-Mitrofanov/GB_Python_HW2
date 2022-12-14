# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

print('Введите число: ')

user_num = int(input())
my_list = [7, 5, 3, 3, 2]

def list_mutate (list, value):
    max_value = max(list)
    if value > max_value:
        list.insert(0, value)
    elif value in list:
        list.insert(list.index(value), value)
    else:
        list.append(value)
    return list

print(list_mutate(my_list, user_num))


