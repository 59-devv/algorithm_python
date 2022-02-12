import copy
from typing import List

# 각 연산을 붙여주는 함수
# 빈 배열과 숫자의 갯수-1 을 넣어준다.
# 숫자가 3개일 경우, 각 숫자에 대한 연산은 두 번 들어가야 하므로


def op(arr: List, num: int) :
    if len(arr) == num:
        op_list.append(copy.deepcopy(arr))
        return
    arr.append(' ')
    op(arr, num)
    arr.pop()

    arr.append('+')
    op(arr, num)
    arr.pop()

    arr.append('-')
    op(arr, num)
    arr.pop()


case_num = int(input())

for _ in range(case_num):
    op_list = list()
    n = int(input())
    num_list = [i for i in range(1, n+1)]
    op([], len(num_list)-1)

    for i in op_list:
        strings = ""

        for j in range(len(i)):
            strings += str(num_list[j]) + i[j]

        strings += str(num_list[-1])

        if eval(strings.replace(" ", "")) == 0:
            print(strings)
    print()
