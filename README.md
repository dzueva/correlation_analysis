#Расчет методом корреляционного анализа
###как запустить программу:
`python3 main.py`\
важно! версия python должна быть не меньше 3.10

###пример использования:
Используем программу для изучения связи между количеством выпитого кофе и производительностью труда. 
В качестве искусственного набора данных мы воспользуемся следующими значениями:\
**Количество чашек кофе в день**: 0, 1, 2, 3, 4, 5, 6.\
**Производительность (задачи, завершенные за день)**: 5, 7, 9, 11, 13, 14, 15.\
\
Запускаем `main.py`:\
\
![example](Images/example.png)

Значение коэффициента корреляции Пирсона r = 0.9914308617264332 указывает на сильную положительную линейную связь между 
количеством выпитого кофе и производительностью труда. Это значит, что с увеличением количества чашек кофе, употребляемых 
в течение дня, обычно повышается производительность труда.
