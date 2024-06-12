from typing import Union
from itertools import count
from math import factorial


DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    def factorial_(y):
        if y == 0 or y == 1:
            return 1
        return factorial_(y - 1) * y
    n = 0
    result = 0
    while True:
        res = ((-1)**n / factorial_(2*n + 1)) * x**(2*n + 1)
        result += res
        n += 1
        if abs(res) < DELTA:
            break
    return result

    # result = 0
    #     term = x  # первый член ряда
    #     n = 1
    #     sign = 1
    #
    #     while abs(term) > DELTA:
    #         result += sign * term
    #         term *= x * x / ((2 * n) * (2 * n + 1))
    #         sign = -sign
    #         n += 1

# print(sinx(0.5))
