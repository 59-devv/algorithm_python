import sys
from typing import List

nums = sys.stdin.readline()
num_list = list(map(int, nums.split()))


def check(list: List) -> str:
    result: int = 0
    for n in range(len(list)-1):
        result += (int(list[n]) - int(list[n+1])) if list[n] > list[n+1]\
            else (int(list[n+1]) - int(list[n]))

    if result == 7 and int(list[0]) == 1:
        return "ascending"
    elif result == 7 and int(list[0]) == 8:
        return "descending"
    return "mixed"


print(check(num_list))