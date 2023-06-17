from math import pi

default_radius = 5


def circle_perimetr(radius=default_radius):
    """Возвращает периметр круга"""
    return 2 * pi * radius


def circle_area(radius=default_radius):
    """Возвращает площадь круга"""
    return pi * radius ** 2