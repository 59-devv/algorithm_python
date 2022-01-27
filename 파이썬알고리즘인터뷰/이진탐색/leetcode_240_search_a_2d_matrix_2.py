# m*n 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라.
# 행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬되어있다.
from typing import List

h = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

target = 5


def find_target2(list: List, target: int) -> bool:

    for l in list:
        left = 0
        right = len(l) - 1

        while left < right:
            center = left + (right - left) // 2
            if l[center] == target:
                return True
            elif l[center] < target:
                left = center + 1
            else:
                right = center

    return False


print(find_target2(h, target))