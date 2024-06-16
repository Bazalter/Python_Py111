from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True

    return False


# print(contains_duplicate([1,2,3,4]))

