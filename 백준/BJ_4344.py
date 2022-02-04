import sys

n = int(sys.stdin.readline())

for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    student_count = data[0]
    average = sum(data[1:]) / student_count
    cnt = 0
    for d in data[1:]:
        if d >= average:
            cnt += 1

    print(f"{(1-(cnt / student_count)) * 100:.3f}%")


