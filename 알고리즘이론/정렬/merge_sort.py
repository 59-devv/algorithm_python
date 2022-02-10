# 병합정렬은 분할정복 알고리즘의 대표적인 예이다.
# 나눌 수 있을만큼 나눈다음,
# 작은 단위로 합치면서 정렬을 반복
# split, merge 두 개의 함수를 재귀호출한다.
import random

data_list = random.sample(range(50), 10)


def merge_split(data):
    if len(data) <= 1:
        return data
    center = len(data) // 2
    left = merge_split(data[:center])
    right = merge_split(data[center:])

    return merge(left, right)


def merge(left, right):
    merged_list = list()
    left_point, right_point = 0, 0

    # 데이터가 둘 다 남아있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged_list.append(right[right_point])
            right_point += 1
        else:
            merged_list.append(left[left_point])
            left_point += 1

    # 왼쪽 데이터만 남아있을 때
    while len(left) > left_point:
        merged_list.append(left[left_point])
        left_point += 1

    while len(right) > right_point:
        merged_list.append(right[right_point])
        right_point += 1

    return merged_list


print(merge_split(data_list))