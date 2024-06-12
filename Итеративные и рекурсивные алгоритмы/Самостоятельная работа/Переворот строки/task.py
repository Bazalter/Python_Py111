from typing import List


def reverse_string(s: List[str]) -> None:
    left_boarder = 0
    right_boarder = len(s) - 1
    while left_boarder < right_boarder:
        s[left_boarder], s[right_boarder] = s[right_boarder], s[left_boarder]
        left_boarder += 1
        right_boarder -= 1
    # return s


# print(reverse_string(["h", "e","l","l","o",]))
