"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError()
    a = None
    b = None
    for i, j in enumerate(arr):
        if a is None:
            a = i
            b = j
        if b > j:
            a = i
            b = j
    return a


print(min_search([-10, -9, 0]))

