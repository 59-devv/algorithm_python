# 배열 안에 2가 있으면 True 를, 아니면 False를 반환하시오.
# 단, 이진탐색을 사용할 것!

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    count = 0
    numbers.sort()
    current_min = numbers[0]
    current_max = numbers[len(numbers)-1]
    current_try_number = (current_min + current_max) //2

    while (current_min <= current_max) :
        count += 1
        if target == current_try_number :
            print(f"{count}번째에 해당 숫자를 찾았습니다.")
            return True
        elif target > current_try_number :
            current_min = current_try_number + 1
        else :
            current_max = current_try_number - 1

        current_try_number = (current_min + current_max) // 2

    return False

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)