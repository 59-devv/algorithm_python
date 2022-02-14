a = input()
b = input()
cnt = 0
pointer = 0

while True:
    if len(a[pointer:]) < len(b):
        break

    if a[pointer:pointer+len(b)] == b:
        cnt += 1
        pointer += len(b)
    else:
        pointer += 1

print(cnt)