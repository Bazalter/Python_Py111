from typing import List
import pprint

def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    ...  # TODO рассчитать таблицу стоимостей перемещений
    n = len(table)
    m = len(table[0])

    table_coast = [[0] * m for i in range(n)]

    table_coast[0][0] = table[0][0]

    for idx in range(1, m):
        table_coast[0][idx] = table_coast[0][idx - 1] + table[0][idx]

    for idx in range(1, n):
        table_coast[idx][0] = table_coast[idx - 1][0] + table[idx][0]

    # pprint.pprint(table_coast, width=20)

    for i in range(1, n):
        for j in range(1, m):
            table_coast[i][j] = min(table_coast[i-1][j], table_coast[i][j-1]) + table[i][j]

    # pprint.pprint(table_coast, width=20)

    return table_coast


if __name__ == '__main__':
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    total_coasts = rocket_coasts(coasts_ceil)
    print(total_coasts[-1][-1])  # 21
