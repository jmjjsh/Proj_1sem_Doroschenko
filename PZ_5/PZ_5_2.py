# Описать функцию Swap(X, Y), меняющую содержимое переменных X и Y (X и Y —
# вещественные параметры, являющиеся одновременно входными и выходными). С
# ее помощью для данных переменных A, B, C, D последовательно поменять
# содержимое следующих пар: A и B, C и D, B и C и вывести новые значения A, B, C,
# D.

while True:
    try:  # обработка исключений
        a, b, c, d = input('Введите a, b, c, d через пробел: ').split()  # Ввод числа
        break
    except ValueError:
        print("Ошибка")


def Swap(x, y):  # функция
    return y, x


a, b = Swap(a, b)
c, d = Swap(c, d)
b, c = Swap(b, c)

print(a, b, c, d)
