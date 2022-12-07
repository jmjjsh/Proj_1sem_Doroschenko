# Дан целочисленный список размера 10. Вывести вначале все содержащиеся в данном
# списке четные числа в порядке возрастания их индексов, а затем — все нечетные
# числа в порядке убывания их индексов.
from random import randint

while True:
    try:  # обработка исключений
        d, w = input('Введите диапазон чисел в списке через пробел: ').split()  # Ввод числа
        break
    except ValueError:
        print("Неверно, попробуйте еще раз!")

list_number = [randint(int(d), int(w)) for i in range(10)]
print(list_number)
print("Четные числа")
for i in list_number:
    if i % 2 == 0:
        print(i)
print("Нечетные числа")
for i in list_number[::-1]:
    if i % 2 != 0:
        print(i)
