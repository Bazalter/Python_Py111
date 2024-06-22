from typing import Tuple
from functools import lru_cache


def calculate_paths(shape: Tuple[int, int]) -> int:
    """
    Дано поле с размером rows*cols посчитать количество ходов коня из верхнего левого угла в нижний правый

    :param shape: размер доски в виде кортежа
    :return: количество путей согласно заданным условиям
    """
    ... # TODO реализуйте подсчет ходов коня

    moves = [(2, 1), (2, -1), (1, 2), (-1, 2)]

    @lru_cache
    def count_path(x, y):
        if x < 0 or x >= shape[0] or y < 0 or y >= shape[1]:
            return 0
        if x == 0 and y == 0:
            return 1
        count = 0
        for move in moves:
            prev_x = x - move[0]
            prev_y = y - move[1]
            count += count_path(prev_x, prev_y)

        return count

    return count_path(shape[0]-1, shape[1]-1)






if __name__ == '__main__':
    print(calculate_paths((4, 4)))  # 2
    print(calculate_paths((7, 15)))  # 13309
