from typing import List


def generate(num_rows: int) -> List[List[int]]:

    if num_rows == 0:
        return []

    if num_rows == 1:
        return [[1]]

    list_pasc = [[1]]

    for i in range(1, num_rows):
        row = [1]
        for j in range(1, i):
            row.append(list_pasc[i-1][j-1] + list_pasc[i-1][j])
        row.append(1)
        list_pasc.append(row)
    return list_pasc




