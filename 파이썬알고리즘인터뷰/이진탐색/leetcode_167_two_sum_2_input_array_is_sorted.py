# 정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를
# 리턴하라. (이 문제에서 배열은 0이 아닌 1부터 시작하는 것으로 한다.)
import bisect

numbers = [2, 7, 11, 15]
target = 9


# 투 포인터로 문제 풀기
def find_two_numbers(numbers: list[int], target: int) -> list[int] :
    left = 0
    right = len(numbers) - 1

    while not left == right:
        sum = numbers[left] + numbers[right]
        if  sum == target:
            return [left+1, right+1]
        elif sum > target:
            right -= 1
        else:
            left += 1


print(find_two_numbers(numbers, target))


# 이진탐색으로 문제 풀기
def find_two_numbers_binary_search(numbers: list[int], target: int) -> list[int]:
    left = 0
    while not left == len(numbers) -1 :
        find_num = target - numbers[left]
        index = bisect.bisect_left(numbers[left+1:], find_num)
        if index is not None:
            return [left+1, index+(left+1)+1]
        else:
            left += 1


print(find_two_numbers_binary_search(numbers, target))