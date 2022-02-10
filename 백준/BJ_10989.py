# 기본 정렬 함수를 사용할 경우, 메모리 초과가 발생한다.
# 데이터가 너무 많아서.
# 다만, 주어진 데이터의 범위가 1~10000 까지로 한정적이기 때문에
# 계수정렬을 이용하면 풀 수 있다.
# 1~10000 까지의 리스를 만들어, 각 index가 숫자를 의미할 수 있도록 만든다.
# 숫자가 반복되면 count 를 늘려주는 방식으로 숫자를 세고
# 숫자만큼 반복해서 출력해주면 풀 수 있다.

import sys

n = int(sys.stdin.readline())
num_list = [0 for x in range(10001)]

for i in range(n):
    num = int(sys.stdin.readline())
    num_list[num] += 1

for i in range(len(num_list)):
    if num_list[i] > 0:
        for k in range(num_list[i]):
            print(i)
