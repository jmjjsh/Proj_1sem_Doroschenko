a = 7
b = 2
c = 8


def triangle_perimetr(a_in=a, b_in=b, c_in=c):
    """Возвращает периметр треугольника"""
    return a_in + b_in + c_in


def triangle_area(a_in=a, b_in=b, c_in=c):
    """Возвращает площадь треугольника"""
    p = (a_in + b_in + c_in) * 0.5
    return (p * (p - a_in) * (p - b_in) * (p - c_in)) ** 0.5
