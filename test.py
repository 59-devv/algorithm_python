# BJ 1920
from typing import *

n: int = int(input())
num_list: List = sorted(list(map(int, input().split(" "))))
m: int = int(input())
target_list: List = list(map(int, input().split(" ")))


def binary(nums: List, target: int):
    left: int = 0
    right: int = len(nums)
    center: int = left + (right - left) // 2

    if nums[center] == target:
        return 1
    if len(nums) == 1 and nums[0] == target:
        return 1
    if len(nums) == 1 and nums[0] != target:
        return 0
    if len(nums) == 0:
        return 0

    if nums[center] > target:
        return binary(nums[:center], target)
    else:
        return binary(nums[center:], target)


for i in target_list:
    print(binary(num_list, i))
