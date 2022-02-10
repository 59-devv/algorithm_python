# input()을 사용할 경우, 간헐적으로 시간초과가 등장한다.
# 어떨땐 통과되고 어떨땐 시간초과.
# sys.stdin.readline()과 속도 비교
# input : stdin.readline() = 4592ms : 384ms
# 10배 가까이 차이가 났다.

import sys

num = int(sys.stdin.readline())
v = []

for i in range(num):
    x, y = sys.stdin.readline().split(" ")
    v.append([int(x), int(y)])

v.sort(key=lambda x: (x[0], x[1]))

for i in v:
    print(i[0], i[1])