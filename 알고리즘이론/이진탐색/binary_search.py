# 중간값 찾기

num_list = [i for i in range(1, 51, 2)]
print(num_list)


def binary_search(nums, target):
    left = 0
    right = len(nums)
    center = left + (right-left) // 2
    print("center : ", nums[center])

    if nums[center] == target:
        print(target)
        return "있음"

    else:
        if len(nums) == 1 and nums[0] == target:
            return "있음"
        if len(nums) == 1 and nums[0] != target:
            return "없음"
        if len(nums) == 0:
            return "없음"

        if nums[center] > target:
            return binary_search(nums[:center], target)
        else:
            return binary_search(nums[center:], target)


result = binary_search(num_list, 41)
print(result)