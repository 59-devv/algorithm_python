import sys

case_count = int(sys.stdin.readline())

# 케이스 수 만큼 반복한다.
for i in range(case_count):
    # 첫 케이스의 데이터 수, 찾고자 하는 문서의 인덱스를 받는다.
    data_count, target_index = map(int, sys.stdin.readline().split(" "))
    # 데이터의 중요도 순서를 입력 받는다.
    data_order = list(map(int, sys.stdin.readline().split(" ")))
    # key, value 형태로 문서의 인덱스와 중요도 순서를 저장한다.
    data = [(idx, value) for idx, value in enumerate(data_order)]

    cnt = 0
    # 반복문을 돌면서
    while True:
        # 저장된 배열에서 중요도가 가장 큰 값을 먼저 확인한다.
        # 람다식을 사용해서 중요도 순으로 정렬한다.
        max_data = max(data, key=lambda item: item[1])
        # 0번째 인덱스의 데이터가 가장 큰 값일 때
        if data[0] == max_data:
            cnt += 1
            # 그 값이 찾고자 하는 값이라면 출력 후 반복문을 종료한다.
            if data[0][0] == target_index:
                print(cnt)
                break
            # 찾고자 하는 값이 아니라면, 뽑아낸다. (Queue)
            else:
                data.pop(0)
        # 0번째 인덱스가 가장 큰 값이 아니라면, 가장 뒤로 보낸다.
        # 이 때, 0번째 값을 뽑아서 가장 뒤로 보낸다.
        else:
            data.append(data.pop(0))
