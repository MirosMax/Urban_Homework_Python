import matplotlib.pyplot as plt
import random

plt.style.use('ggplot')  # стиль графиков

fig, axes = plt.subplots(2, 2)  # создаем рисунок fig и 4 графика на нем


x_1 = [i for i in range(-10, 11)]
y_1 = [i ** 2 for i in x_1]
y_2 = [abs(i) for i in x_1]
y_3 = [random.randint(1, 30) for i in range(21)]

labels = 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь'
data = [13, 8, 10, 3, 20, 7]
explode = (0.1, 0, 0, 0, 0.15, 0)

axes[0][0].plot(x_1, y_1)  # рисуем параболу на первом поле
axes[0][1].plot(x_1, y_2, color='green', linestyle='dotted')  # зеленый график точками на 2 поле
axes[1][0].plot(x_1, y_3, color='blue', linestyle='-')  # синий график прерывистой линией на 3 поле
axes[1][1].pie(data, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')  # круговая диаграмма на 4 поле

plt.show()
