# Расчет методом корреляционного анализа
### как запустить программу:
установить все нужные библиотеки:\
`pip install --no-cache-dir -r requirements.txt`\
запустить скрипт:\
`python3 main.py`\
(важно! версия python должна быть не меньше 3)

### пример использования:

Давайте рассмотрим пример, где мы имеем таблицу с данными о расходах потребителей на различные категории продуктов питания за неделю, а также общий бюджет на питание на неделю для каждого потребителя:

```
         Потребитель 1    Потребитель 2    Потребитель 3    Потребитель 4    Потребитель 5    Общий бюджет
Молоко             5                4                3                6                5             30
Хлеб               2                3                1                2                4             12
Мясо               10               8                5                12               9             44
Фрукты             7                6                4                8                5             30
```

Мы можем проанализировать, как наличие детей влияет на структуру потребления продуктов питания по категориям. Например, мы можем посчитать среднее количество детей для каждого потребителя, а затем разделить таблицу на две группы - семьи с детьми и без детей. Затем мы можем рассчитать средние значения расходов каждой группы на каждую категорию продуктов питания и сравнить их. Это может помочь нам ответить на вопрос, каким образом присутствие детей влияет на потребление молока, хлеба, мяса и фруктов.

Выходные данные могут выглядеть так:

```
Средние значения расходов на неделю для семей с детьми:
Потребитель 1    6.0
Потребитель 2    3.5
Потребитель 3    2.5
Потребитель 4    9.0
Потребитель 5    4.5
Общий бюджет     28.0
Дети              2.0
dtype: float64

Средние значения расходов на неделю для семей без детей:
Потребитель 1    3.5
Потребитель 2    2.0
Потребитель 3    3.0
Потребитель 4    7.0
Потребитель 5    4.5
Общий бюджет     20.0
Дети              0.0
dtype: float64
```

Мы видим, что семьи с детьми тратят больше на молоко и фрукты, чем семьи без детей, тогда как семьи без детей тратят больше на хлеб и мясо.

