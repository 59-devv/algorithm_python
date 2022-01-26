# 두 배열의 교집합을 구하시오.

import bisect
from typing import Set

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]

result: Set = set()
nums2.sort()
for n in nums1:
    index = bisect.bisect_left(nums2, n)
    if nums2[index] == n:
        result.add(n)

print(result)


result2: Set = set()
nums4.sort()
for n2 in nums3:
    index2 = bisect.bisect_left(nums4, n2)
    if nums4[index2] == n2:
        result2.add(n2)

print(result2)