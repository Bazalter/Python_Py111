from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    min_index, max_index = 0, len(seq)-1

    while min_index <= max_index:
        middle_index = min_index + (max_index - min_index) // 2
        middle_value = seq[middle_index]

        if value == middle_value:
            while True:
                if not 0 <= middle_index - 1 < len(seq) or seq[middle_index - 1] != value:
                    break
                else:
                    middle_index -= 1
            return middle_index

        if middle_value > value:
            max_index = middle_index - 1
        else:
            min_index = middle_index + 1

    raise ValueError('Нет элемента')



# print(binary_search(1001, [1000, 1001]))
