# 퀵정렬은 특이상황의 경우 O(n2)까지 시간복잡도가 올라간다.
# 즉, 피봇이 가장 크거나 가장 작을 때...
# 가장 앞에 피봇을 세우고
# 피봇을 기준으로 작은 수는 피봇의 앞에,
# 피봇을 기준으로 큰 수는 피봇의 뒤에 위치시킨다.
# 정렬이 완료될 때까지 재귀함수로 호출한다.

import random

num_list = random.sample(range(100), 10)


def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if item > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort(num_list))
