# 데이터가 두 개일 때
import random

data = [5, 2]

for i in range(len(data) - 1):
    if data[i] > data[i + 1]:
        data[i], data[i + 1] = data[i + 1], data[i]

print(data)

# 데이터가 세 개일 때
data = [4, 3, 5]

for i in range(len(data) - 1):
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print(data)

# 데이터가 네 개일 때
data = [5, 2, 3, 1]

for i in range(len(data) - 1):
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print(data)

# 정렬이 필요하지 않을 땐 그냥 종료하게 만들기
data = [5, 2, 3, 1]

for i in range(len(data) - 1):
    swap = False
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            swap = True
    if not swap:
        break

print(data)

# 랜덤 데이터로 확인
data = random.sample(range(100), 50)
for i in range(len(data) - 1):
    swap = False
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            swap = True
    if not swap:
        break

print(data)