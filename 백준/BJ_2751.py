n = int(input())
num_list = []

for i in range(n):
    num = int(input())
    num_list.append(num)


def qsort(data):
    if len(data) <=1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])

    return qsort(left) + [pivot] + qsort(right)


for i in qsort(num_list):
    print(i)