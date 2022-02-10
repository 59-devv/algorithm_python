# 동적 계획법
# 점화식을 찾는 것이 중요하다.
# 손으로 작은 수 부터 확인해보고, 패턴을 빠르게 찾아내는 것이 좋다.

n = int(input())
dp = [0] * (1000+1)

def calc(n):
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


print(calc(9) % 10007)