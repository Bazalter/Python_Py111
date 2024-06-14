from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    for j in range(len(container)-1):
        for i in range(len(container) - 1 - j):  # TODO реализовать алгоритм сортировки пузырьком
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]

    return container


print(sort([6,5,3,2,5,4,7]))