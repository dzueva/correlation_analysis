#!/usr/bin/python3
import math


def pearson_correlation(data_first: list[float], data_second: list[float]):
    """Расчет коэффициента корреляции Пирсона"""
    if len(data_first) != len(data_second):
        raise ValueError("У первого и второго набора данных должна быть одна и та же длина!")

    n = len(data_first)
    sum_x = sum(data_first)
    sum_y = sum(data_second)
    sum_xy = sum([xi * yi for xi, yi in zip(data_first, data_second)])
    sum_x_squared = sum([xi ** 2 for xi in data_first])
    sum_y_squared = sum([yi ** 2 for yi in data_second])

    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2))

    if denominator == 0:
        return 0

    return numerator / denominator


def formatting(data: str) -> list[float]:
    """Обработка введенных данных"""
    result_list = data.split()
    for i in range(len(result_list)):
        result_list[i] = float(result_list[i])
    return result_list


if __name__ == '__main__':
    data_first_input = formatting(input('Введите набор данных для первой переменной (в виде списка чисел, разделяя элементы пробелами): '))
    data_second_input = formatting(input('Введите набор данных для второй переменной (в виде списка чисел, разделяя элементы пробелами): '))
    r = pearson_correlation(data_first_input, data_second_input)
    print('')
    print(f'Значение коэффициента корреляции Пирсона для двух предоставленных наборов данных: {r}')
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
