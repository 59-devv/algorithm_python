import sys

case_count = int(sys.stdin.readline())

for i in range(case_count):
    cnt = 0
    data_count, target_index = map(int, sys.stdin.readline().split(" "))
    data_order = list(map(int, sys.stdin.readline().split(" ")))
    data = []
    for j in range(data_count):
        data.append([j, data_order[j]])

    while len(data) != 0:
        max_data = max(data, key=lambda item: item[1])
        if data[0] == max_data:
            cnt += 1
            if data[0][0] == target_index:
                print(cnt)
                break
            else:
                data.pop(0)
        else:
            data.append(data.pop(0))
