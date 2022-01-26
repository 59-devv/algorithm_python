# 특정 피벗을 기준으로 회전하여 정렬된 배열에서, target 값의 인덱스를 출력하라.
import bisect
from typing import List

## 풀이 1번. binary search 직접 구현

nums = [4, 5, 6, 7, 0, 1, 2]
target = 1

# 정렬된 입력값에서 특정 피벗을 기준으로 회전되었기 때문에,
# 최솟값을 찾아서 다시 정렬해야 한다.
# 우선, 이진탐색을 통해서 최솟값을 찾아야 한다.

# 1. 최솟값 찾기
def find_min_number(nums: List[int]) -> int:
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1

    while left < right:
        center = left + (right - left) // 2
        if nums[center] > nums[right]:
            left = center + 1
        else:
            right = center

    return center


# 2. 오름차순으로 정렬하기
def sort_list(nums: List[int], center: int) -> List[int]:
    if not nums:
        return []

    sorted_nums = nums[center:] + nums[:center]
    return sorted_nums


# 3. 타겟의 index 찾기
def find_target_index_binary_search(sorted_nums: List[int], target: int) -> int:
    if not sorted_nums:
        return -1

    left = 0
    right = len(sorted_nums) - 1

    while left < right:
        center = left + (right - left) // 2
        if sorted_nums[center] == target:
            return center
        elif sorted_nums[center] > target:
            right = center
        else:
            left = center + 1

    return -1


min_num_index = find_min_number(nums)
sorted_list = sort_list(nums, min_num_index)
result = find_target_index_binary_search(sorted_list, target)

# 이전에 찾았던 최솟값 인덱스에서 더해줘야한다. (피벗을 기준으로 회전했으므로)
final_result = min_num_index + result

 ###############################################################################


## 풀이 2번. 파이썬 함수를 이용한 정렬 및 이진탐색

nums = [4, 5, 6, 7, 0, 1, 2]
target = 1

# 최소값 찾기
min_num = min(nums)
# 최소값의 인덱스 찾기
min_num_index = nums.index(min_num)

# bisect.bisect_left(배열, 타겟) : 배열에서 타겟을 찾는다. 인덱스를 리턴한다.
# 타겟이 여러개면 왼쪽 인덱스를 리턴한다.
def binary_search_with_bisect(nums: List[int], target: int) -> int:
    nums.sort()
    index = bisect.bisect_left(nums, target)

    return index

result2 = binary_search_with_bisect(nums, target)
final_result2 = result2 + min_num_index
print(final_result2)
