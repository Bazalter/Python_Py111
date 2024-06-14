# from typing import List
#
#
# def sort(container: List[int]) -> List[int]:
#     """
#     Алгоритм быстрой сортировки.
#
#     1. Выбираем опорный элемент. Например, первый элемент.
#     2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
#     3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.
#
#     :param container: последовательность, которую надо отсортировать
#     :return: Отсортированная в порядке возрастания последовательность
#     """
#     if len(container) <= 1:  # TODO реализовать алгоритм быстрой сортировки
#         return container
#     else:
#         pivot = container[len(container) // 2]
#         left = [x for x in container if x < pivot]
#         mid = [x for x in container if x == pivot]
#         right = [x for x in container if x > pivot]
#         return sort(left) + mid + sort(right)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_in_place(arr, low, pi - 1)
        quicksort_in_place(arr, pi + 1, high)


# Пример использования
arr = [3, 6, 8, 10, 1, 2, 11]
# print(partition(arr,0,6))
print("Неотсортированный массив:", arr)
quicksort_in_place(arr, 0, len(arr) - 1)
print("Отсортированный массив:", arr)