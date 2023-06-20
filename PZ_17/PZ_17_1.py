# Создайте класс "Калькулятор" с методами "сложение", "вычитание", "умножение" и
# "деление". Каждый метод должен принимать два аргумента и возвращать результат
# операции.
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, a='', b=''):
        if not a:
            a = self.a
        if not b:
            b = self.b
        print(f'a={a} и b={b}')
        return f'Сумма элементов: {a + b}'

    def sub(self, a='', b=''):
        if not a:
            a = self.a
        if not b:
            b = self.b
        print(f'a={a} и b={b}')
        return f'Разность элементов: {b - a if b > a else a - b}'

    def mul(self, a='', b=''):
        if not a:
            a = self.a
        if not b:
            b = self.b
        print(f'a={a} и b={b}')
        return f'Умножение элементов: {a * b}'

    def dec(self, a='', b=''):
        if not a:
            if self.a != 0:
                a = self.a
            else:
                return 'Делитель не должен быть равен 0!'
        if not b:
            b = self.b
        print(f'Вы ввели a={a} и b={b}')
        return f'Деление элементов: {a / b}' if a > 0 else 'Делитель не должен быть равен 0!'


c = Calculator(3, 6)
print(c.add(1))
print(c.sub(6))
print(c.mul(6, 2))
print(c.dec(5))
