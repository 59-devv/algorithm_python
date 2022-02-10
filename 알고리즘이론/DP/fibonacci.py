# 피보나치 수열
# 재귀호출을 사용하면, 계속해서 fibo 함수를 재실행해야함
# 이전에 계산했던 값을 재활용하지 못함

def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1) + fibo(num-2)


print(fibo(10))


# 위같은 문제를 해결하기 위해 Dynamic Programming 활용
# DP는 Memorization 기법을 사용하여, 이전의 연산 결과를 저장하고 재활용함
# 각 순서를 index로 활용한 배열을 생성하고,
# 연산 값을 배열에 저장해두고 재활용한다.
def fibo_dp(num):
    cache = [0 for i in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for i in range(2, num+1):
        cache[i] = cache[i-1] + cache[i-2]

    return cache[num]


print(fibo_dp(10))