n = int(input())
dp = [0] * (100+1)


def solution(num):
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    if num >= 6:
        for i in range(6, num+1):
            dp[i] = dp[i-1] + dp[i-5]

    return dp[num]


for _ in range(n):
    number = int(input())
    print(solution(number))

