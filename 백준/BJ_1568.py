n = int(input())
cnt = 0
delete_num = 1

while n != 0:
    if n >= delete_num:
        n -= delete_num
        delete_num += 1
        cnt += 1
    else:
        delete_num = 1


print(cnt)