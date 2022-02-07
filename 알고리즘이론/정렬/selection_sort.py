# 주어진 데이터 중 최소값을 찾는다.
# 최소값을, 범위의 가장 앞으로 정렬시킨다.
# 반복한다.

# 랜덤 데이터로 바로 코드 구현
import random

data = random.sample(range(100), 10)

for i in range(len(data)-1):
    min_data = i
    for j in range(i+1, len(data)):
        if data[j] < data[min_data]:
            min_data = j

    data[i], data[min_data] = data[min_data], data[i]


print(data)