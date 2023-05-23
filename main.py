#!/usr/bin/python3
import pandas as pd
from tabulate import tabulate


if __name__ == '__main__':
    data = {
        'Потребитель 1': [5, 2, 10, 7],
        'Потребитель 2': [4, 3, 8, 6],
        'Потребитель 3': [3, 1, 5, 4],
        'Потребитель 4': [6, 2, 12, 8],
        'Потребитель 5': [5, 4, 9, 5],
        'Общий бюджет': [30, 12, 44, 30],
    }
    indexes = ['Молоко', 'Хлеб', 'Мясо', 'Фрукты']
    additional_data = {'Дети': [2, 0, 1, 3, 0]}
    col_names = ['']
    for key in data.keys():
        col_names.append(key)
    table_data = []
    for index in range(len(indexes)):
        raw = [indexes[index]]
        for key, value in data.items():
            raw.append(value[index])
        table_data.append(raw)

    print(tabulate(table_data, headers=col_names, tablefmt="fancy_grid"))
    print('')

    df = pd.DataFrame(data, index=indexes)
    additional_name = list(additional_data.keys())[0]
    # Рассчитываем среднее количество детей на каждого потребителя
    df[additional_name] = additional_data.get(additional_name)

    # Разделяем таблицу на две группы - семьи с детьми и без детей
    with_kids = df[df[additional_name] > 0]
    no_kids = df[df[additional_name] == 0]

    # Считаем средние значения расходов каждой группы на каждую категорию продуктов питания
    with_kids_means = with_kids.mean()
    no_kids_means = no_kids.mean()

    # Выводим результаты анализа данных
    print("Средние значения расходов на неделю для семей с детьми:")
    print(with_kids_means)
    print('')
    print("Средние значения расходов на неделю для семей без детей:")
    print(no_kids_means)
