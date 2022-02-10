# 피보나치

result = []
num = int(input())

for i in range(num+1):
    if i <= 1:
        result.append(i)
    else:
        result.append(result[i-1] + result[i-2])

print(result[num])
