# В матрице элементы второго столбца заменить элементами из одномерного
# динамического массива соответствующей размерности.

import random

x = random.randint(2, 5)
y = random.randint(2, 5)
matrix = [[random.randint(-10, 10) for j in range(x)] for i in range(y)]
xx = [random.randint(-10, 10) for item in range(y)]

print('матрица до:', matrix)
print('динамический массив:', xx)
print('матрица после:', [[xx[matrix.index(i)] if i.index(k) == 1 else k for k in i] for i in matrix])
