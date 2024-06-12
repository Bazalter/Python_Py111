from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    dict_ = {}
    for index, x in enumerate(nums):
        y = target - x
        if y in dict_:
            return [dict_[y], index]
        if x not in dict_:
            dict_[x] = index
    return []


# print(two_sum([2,7,11,15], 9))



# d = {1:2, 3:1, 2:4}
#
# print(2 in d)