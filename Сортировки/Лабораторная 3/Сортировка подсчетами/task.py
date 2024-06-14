from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container
    min_val = min(container)
    max_val = max(container)
    count_ran = [0] * (max_val-min_val + 1)
    # print(count_ran)

    for i in container:
        count_ran[i - min_val] +=1
    # print(count_ran)

    for i in range(1, len(count_ran)):
        count_ran[i] += count_ran[i - 1]
    # print(count_ran)

    result = [0] * len(container)

    for i in reversed(container):
        result[count_ran[i - min_val] - 1] = i
        count_ran[i - min_val] -= 1

    return result


# print(sort([2,2,2,2,3,3,3,5,6,7,7,8,8,8,9,9,9,10,10,10]))
