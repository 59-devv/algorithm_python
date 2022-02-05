import sys

a = list(map(int, sys.stdin.readline().split()))
num_list = list(map(int, sys.stdin.readline().split()))
num = a[0]
limit = int(a[1])
max = 0

for i in range(0, len(num_list)-2):
    for j in range(i+1, len(num_list)-1):
        for k in range(j+1, len(num_list)):
                sum = num_list[i] + num_list[j] + num_list[k]
                if max < sum <= limit:
                    max = sum

print(max)