# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
# Каждый кортеж хранит информацию об отдельном товаре. 
# В кортеже должно быть два элемента — номер товара и словарь с параметрами 
# (характеристиками товара: название, цена, количество, единица измерения). 
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

print('Сколько планируется товаров?')
goods_number = int(input())

goods = []
good_id = 0
while good_id < goods_number:
    good_id += 1
    good_features = {}
    while input("Хотите ввести данные товара в формате 'ключ' : 'значение'? Да | Нет: ") == 'Да':
        good_key = input("Введите название характеристики: ")
        good_value = input("Введите значение: ")
        good_features[good_key] = good_value
    goods.append(tuple([good_id, good_features]))
    
print(goods)

def analitics (goods):
    summary = {}
    for good in goods:
        for good_key, good_value in good[1].items():
            if good_key in summary:
                summary[good_key].append(good_value)
            else:
                summary[good_key] = [good_value]
    print(summary)

analitics(goods)


