# Составить программу, в которой функция
# генерирует четырехзначное число и
# определяет, есть ли в числе одинаковые цифры
from random import randint


def get_integer():  # функция
    number = str(randint(1111, 9999))
    get_set = {number[0], number[1], number[2], number[3]}
    if len(get_set) != len(number):  # условие
        return f'В числе {number} есть одинаковые цифры'
    else:
        return f'В числе {number} нет одинаковых цифр'


print(get_integer())
