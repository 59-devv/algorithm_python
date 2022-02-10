# DP

import sys

n = int(sys.stdin.readline())


# 메모리 초과가 발생하는 이유
# n의 범위가 1,000,000까지 이기 때문에, 연산을 하다보면
# int의 범위를 넘어서게 된다.
# 따라서 변수에 할당하기 전에, 미리 나머지 연산을 해주어야 한다.

def solution(num):
    dp = [0] * (n + 1)
    dp[1] = 1
    if num >= 2:
        for i in range(2, num+1):
            dp[i] = dp[i-1] + dp[i-2] % 15746

    return dp[num]


print(solution(n))