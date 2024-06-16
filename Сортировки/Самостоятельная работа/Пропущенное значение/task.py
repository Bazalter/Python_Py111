from typing import List


def missing_number(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    if nums[0] != 0:
        return 0

    if nums[-1] != n:
        return n

    for i in range(1, n):
        if nums[i] != i:
            return i

# print(missing_number([9,6,4,2,3,5,7,0,1]))



