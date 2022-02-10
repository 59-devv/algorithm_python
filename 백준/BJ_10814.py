n = int(input())
result = []


for i in range(n):
    age, name = input().split(" ")
    result.append([age, name])


result.sort(key=lambda item: item[0])

for i in result:
    print(i[0], i[1])
