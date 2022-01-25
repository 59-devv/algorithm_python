# 정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾으시오.

nums = [-1, 0, 3, 5, 9, 12]
target = 9

def binary_search(nums, target) :
    left = 0
    right = len(nums)-1

    while left < right:
        center = left + (right - left) // 2
        if target == nums[center]:
            print(center)
            return
        elif target > nums[center]:
            left = center + 1
        else:
            right = center

binary_search(nums, target)


