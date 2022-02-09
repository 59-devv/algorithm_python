n = int(input())
num_list = []

for i in range(n):
    num = int(input())
    num_list.append(num)

# 파이썬 내장 함수 이용
# result = sorted(num_list)
# for i in result:
#     print(i)


# 삽입정렬
for j in range(len(num_list) - 1):
    for k in range(j + 1, 0, -1):
        if num_list[k] < num_list[k - 1]:
            num_list[k], num_list[k - 1] = num_list[k - 1], num_list[k]
        else:
            break

for i in num_list:
    print(i)
