from typing import List


def majority_element(nums: List[int]) -> int:
    count = 0
    maj_elem = 0
    for i in nums:
        if count == 0:
            maj_elem = i
            count = 1
        elif i == maj_elem:
            count += 1
        else:
            count -= 1


    if count == 0:
        return None
    else:
        return maj_elem

# print(majority_element( [2,2,1,1,1,2,2]))