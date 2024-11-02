def find_first_item(list_items, item):
    for i in range(len(list_items)):  # Проверяет каждый индекс из словаря
        if list_items[i] == item:  # Сравнивает идекс общего списка товаров с названием товаров из нашего списка
            return i  # Возвращает индекс первого вхождения нашего товара в общий список
    return None  # Вовзращает None, если не находит наш товар


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_item(items_list, find_item)  # Присвоение результатов функции переменной "index_item"
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
