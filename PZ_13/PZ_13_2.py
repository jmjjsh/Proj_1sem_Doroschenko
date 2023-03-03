# В матрице найти среднее арифметическое положительных элементов, кратных 3.

import random
from functools import reduce

count = 0
dec = []
total = 0
while count < 3:
    a = [random.randint(-10, 10) for n in range(0, 3)]
    count += 1
    dec.append(a)
print('матрица: ', dec)
for i in dec:
    x = list(filter(lambda v: v % 3 == 0, i))
    nue = list(filter(lambda v: v > 0, x))
    if len(nue) != 0:
        total += reduce(lambda v, y: v + y, x)
print('cреднее арифметическое положительных элементов, кратных 3: ', total)
