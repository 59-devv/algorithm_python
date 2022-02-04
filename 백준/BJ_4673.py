# self number

num_list = list(range(1, 10001))


def calculate_self_num(num: int):
    str_num = str(num)
    new_num = num
    for i in range(len(str_num)):
        new_num += int(str_num[i])
    try:
        num_list.remove(new_num)
    except ValueError:
        pass


for x in range(1, 10001):
    calculate_self_num(x)

for y in num_list:
    print(y)
