"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
        self.deque_priority = {i: deque() for i in range(self.LOW_PRIORITY+1)}  # TODO использовать deque для реализации очереди с приоритетами

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        self.deque_priority[priority].append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        for i in self.deque_priority.values():
            if i:
                return i.popleft()
        raise IndexError()

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):  # TODO реализовать метод peek
            raise TypeError()
        queue = self.deque_priority[priority]
        if not 0 <= ind < len(queue):
            raise IndexError()

        return queue[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        for queue in self.deque_priority.values(): # TODO реализовать метод clear
            queue.clear()


    def __len__(self):
        """ Количество элементов в очереди. """
        # TODO реализовать метод __len__
        len_ = 0
        for i in self.deque_priority.values():
            len_ +=len(i)
        return len_

