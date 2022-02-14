# BJ_11004
# 정렬 문제인데 데이터의 수가 많기 때문에 효율적으로 정렬해야한다.
# 파이썬의 기본 내장 sorted() 함수는 효율이 굉장히 좋기 때문에, 그냥 사용해도 된다.
# 하지만 병합정렬 복습 겸 한번 더 구현해보도록 한다.
# (참고 : 병합정렬은 python3로 제출할 경우 시간초과로 테스트 실패할 수도 있음)
# (이 때, pypy3로 제출하면 메모리는 더 많이 사용하지만 시간은 조금 빠르기 때문에 성공할 수도 있음)
from typing import List


def merge_sort(arr: List):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

    return arr


num, index = map(int, input().split(" "))
num_list = list(map(int, input().split(" ")))

# 두 가지 모두 사용해서 정렬해본다.
# 1. 파이썬 내장 함수 sorted()
# 2. 위에서 만든 병합정렬
result = sorted(num_list)
result2 = merge_sort(num_list)


# 정렬해서 index 번째 수를 출력하면 된다.
# 단, index는 1부터 시작한다.
print(result[index-1])
print(result2[index-1])