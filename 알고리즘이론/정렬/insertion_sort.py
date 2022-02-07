# 데이터를 특정 위치에 삽입함
# 두번째 데이터부터 시작해서, 앞 데이터와 비교함
# 정렬되지 않은 데이터들까지 쭉 비교해서, 본인의 자리를 찾아감
# 어느자리에 삽입되어야 하는지를 찾는다고 해서 삽입 정렬


# 랜덤 데이터로 바로 코드 구현
import random

data = random.sample(range(100), 50)
print(data)

for i in range(len(data)-1):
    # i+1 부터 시작해서, 한 칸씩 앞으로 가는 반복문을 만들어준다.
    for j in range(i + 1, 0, -1):
        if data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
        else:
            # 앞이 더 작으면, 이미 다 정렬이 된 부분이므로 반복문 종료
            break

print(data)