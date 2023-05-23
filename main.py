#!/usr/bin/python3
import pandas as pd
import numpy as np


def coeff_meaning(r: float):
    """Интерпретация значения коэффициента Пирсона"""
    if r == 0:
        print("Нет линейной связи между переменными")
    elif 0 < r < 0.3:
        print("Слабая положительная линейная связь между переменными")
    elif 0.3 <= r < 0.5:
        print("Умеренная положительная линейная связь между переменными")
    elif 0.5 <= r < 0.7:
        print("Заметная положительная линейная связь между переменными")
    elif 0.7 <= r < 0.9:
        print("Высокая положительная линейная связь между переменными")
    elif 0.9 <= r <= 1:
        print("Очень высокая положительная линейная связь между переменными")
    elif 0 > r > -0.3:
        print("Умеренная отрицательная линейная связь между переменными")
    elif -0.3 >= r > -0.5:
        print("Заметная отрицательная линейная связь между переменными")
    elif -0.5 >= r > -0.7:
        print("Высокая отрицательная линейная связь между переменными")
    elif -0.7 >= r > -0.9:
        print("Очень высокая отрицательная линейная связь между переменными")
    elif -0.9 >= r >= -1:
        print("Полная отрицательная линейная связь между переменными")


def formatting(_data: str):
    """Обработка введенных данных"""
    result_list = _data.split()
    for i in range(len(result_list)):
        result_list[i] = float(result_list[i])
    return result_list


if __name__ == '__main__':
    data_first_name = input('Введите описание первого набора данных (например: "Количество чашек кофе в день"): ')
    data_second_name = input('Введите описание второго набора данных (например: "Производительность"): ')

    data_first_input = formatting(input('Введите набор данных для первой переменной (в виде списка чисел, разделяя элементы пробелами): '))
    data_second_input = formatting(input('Введите набор данных для второй переменной (в виде списка чисел, разделяя элементы пробелами): '))

    # Создание набора данных
    data = {data_first_name: data_first_input,
            data_second_name: data_second_input}
    df = pd.DataFrame(data)

    # Описательная статистика
    print(df.describe())

    # Рассчитываем коэффициент корреляции Пирсона
    corr = np.corrcoef(df[data_first_name], df[data_second_name])[0, 1]
    print("Коэффициент корреляции Пирсона: ", corr)
    coeff_meaning(corr)

