from typing import List

n = int(input())
n_list = list()

for _ in range(n):
    n_list.append(int(input()))

result_list = list()


def left(num_list: List):
    max_num = max(num_list)
    cnt = 0
    current_max = 0
    for i in num_list:
        if i == max_num:
            cnt += 1
            result_list.append(cnt)
            break
        else:
            if i <= current_max:
                continue
            else:
                current_max = i
                cnt += 1


def right(num_list: List):
    num_list.reverse()
    max_num = max(num_list)
    cnt = 0
    current_max = 0
    for i in num_list:
        if i == max_num:
            cnt += 1
            result_list.append(cnt)
            break
        else:
            if i <= current_max:
                continue
            else:
                current_max = i
                cnt += 1


left(n_list)
right(n_list)

for i in result_list:
    print(i)
