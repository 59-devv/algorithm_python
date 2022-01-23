finding_target = 30
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    cnt = 0
    current_min = array[0]
    current_max = array[len(array)-1]
    current_tryNum = (current_max + current_min) // 2

    while (current_min <= current_max) :
        cnt += 1
        if target > current_tryNum :
            current_min = current_tryNum + 1
        elif target < current_tryNum :
            current_max = current_tryNum - 1
        else :
            print(cnt)
            return True

        current_tryNum = (current_max + current_min) // 2
        print(cnt)
    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)