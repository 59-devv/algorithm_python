a = input()

# 파이썬 내장 함수로 쉽게 풀기
# b = list(str(a))
#
# b.sort(reverse=True)
# b = "".join(b)
#
# print(int(b))


# 자리수의 숫자를 이용해서 풀기
for i in range(9, -1, -1):
    for j in a:
        if int(j) == i:
            print(int(j), end="")

