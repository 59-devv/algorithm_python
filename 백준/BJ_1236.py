num, length = map(int, input().split(" "))
arrays = list()

for i in range(num):
    data = input()
    arrays.append(data)


y_guard = 0
for i in range(len(arrays[0])):
    is_guard = False
    for j in range(len(arrays)):
        if arrays[j][i] == "X":
            is_guard = True
    if is_guard is False:
        y_guard += 1


x_guard = 0
for i in arrays:
    if "X" not in i:
        x_guard += 1


print(max(x_guard, y_guard))