input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    # 첫번째 숫에 따라, 변환시켜줘야하는 카운트를 1 증가시켜줘야 한다.
    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    # 다음 수가 같지 않을 경우, 변환 카운트를 1씩 증가시켜준다.
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    # 둘 중, 최소값을 찾는다.
    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)