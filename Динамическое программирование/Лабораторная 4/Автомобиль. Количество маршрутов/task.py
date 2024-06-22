from typing import List
import pprint

def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования

    result = [[0]*n for i in range(m)]
    # pprint.pprint(result, width=20)

    for i in range(n):
        result[0][i] = 1

    # pprint.pprint(result, width=20)

    for i in range(1, m):
        result[i][0] = 1

    # pprint.pprint(result, width=20)

    for i in range(1, m):
        for j in range(1, n):
            result[i][j] = result[i-1][j] + result[i][j-1] + result[i-1][j-1]

    pprint.pprint(result, width=20)
    return result



if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
