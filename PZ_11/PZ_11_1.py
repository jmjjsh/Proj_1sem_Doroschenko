from random import randint

f1 = open('n_1.txt', 'w')  # создание первого файла
f1.write(' '.join([str(randint(-100, 100)) for i in range(10)]))  # добавление данных в файл
f1.close()

f2 = open('n_2.txt', 'w', encoding='UTF-8')  # создание заполняемого файла
f3 = open('n_1.txt', 'r', encoding='UTF-8').read()  # чтение первого файла

len_n = len(f3.split(' '))  # получаем количество элементов
index_max = f3.split().index(str(max([int(x) for x in f3.split(' ')])))
smena = [int(i) for i in f3.split(' ')]

print(f'Исходные данные: {f3}\n'
      f'Количество элементов: {len_n}\n'
      f'Индекс последнего максимального элемента:{index_max}\n'
      f'Меняем местами первую и последнюю трети:{smena[6:] + smena[4:6] + smena[0:4]}')

