# 수 찾기
import sys

n = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().split(" ")))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split(" ")))
result = []

for i in range(m):
    if b[i] in a:
        result.append("1")
    else:
        result.append("0")

print("\n".join(result))


# in 연산자를 통해 값이 있는 여부를 확인할 경우,
# list 는 O(n), set은 O(1) 이다.
# set이 해시 함수, 해시 테이블을 이용해서 만든 것이기 때문이다.