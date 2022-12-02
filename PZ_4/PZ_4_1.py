# 1. Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N

n = input('введите число : ')

while type(n) != int:  # обработчик исключений
    try:
        n = int(n)
    except ValueError:
        print('неверно')
        n = input('введите число N: ')

i = 0
while i in range(n):  # цикл while с последовательностью до n
    i += 1
    x = i + (1 / 2)
# noinspection PyUnboundLocalVariable
print(f"сумма N = {x}")
