import sys

n = int(sys.stdin.readline())
stack = []
result = []
cnt = 1

# 첫번째 받은 숫자만큼 반복한다.
for i in range(1, n + 1):
    # 숫자를 입력 받는다.
    num = int(sys.stdin.readline())
    # 현재 stack에 쌓아야 할 숫자가 몇인지 cnt로 계산한다.
    # cnt가 입력받은 숫자일때까지 stack에 쌓고,
    # 입력 받은 숫자가 cnt보다 작을 경우에는 stack에서 뽑아낸다.
    # 이 과정을 반복하면 결과를 출력할 수 있다.
    while cnt <= num:
        stack.append(cnt)
        cnt += 1
        result.append('+')
    if num == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        # 아래 구문들을 모두 실행시키지 않고, 프로그램을 바로 종료시킨다.
        exit(0)

print("\n".join(result))
