num = int(input())
origin_num = num


def calculate_until_same(num: int) -> int:
    cnt = 0

    while True:
        cnt += 1
        if num < 10:
            result = int(str(num) + str(num))
        else:
            new_num = int(str(num)[0]) + int(str(num)[1])
            result = int(str(num)[1] + str(new_num)[0]) if new_num < 10 \
                else int(str(num)[1] + str(new_num)[1])

        if origin_num == result:
            return cnt
        else:
            num = result

    return cnt


print(calculate_until_same(num))
