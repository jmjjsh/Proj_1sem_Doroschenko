#Дано множество A из N точек на плоскости и точка B (точки заданы своими
#координатами х, у). Найти точку из множества A, наиболее близкую к точке B.
#Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по
#формуле:
#R = √(x2 – x1)2 + (у2 – y1)2
#Для хранения данных о каждом наборе точек следует использовать по два список: первый
#список для хранения абсцисс, второй — для хранения ординат.
from math import sqrt
from random import randint

while True:
    try:  # обработка исключений
        N = int(input('Ведите длинну списка: '))
        x_b, y_b = input('Введите координаты точки B: ').split()  # Ввод числа
        break
    except ValueError:
        print("Не корректный ввод, попробуйте еще раз!")

x = [randint(1, 100) for i in range(N)]
print(x)
y = [randint(1, 100) for i in range(N)]
print(y)
list_r = []
for i in range(N):

    list_r.append((sqrt(((int(x_b) - x[i])**2))) + ((int(y_b) - y[i])**2))
print(list_r)
print(f'Координаты точки, наиболее близкой к точке'
      f' B: x - {x[list_r.index(min(list_r))]}, y - {y[list_r.index(min(list_r))]}')