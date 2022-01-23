# 가장 긴 팰린드롬 부분 문자열을 출력하라.

# 예시
input1 = "babad"
output1 = "bab"

input2 = "cbbd"
output2 = "bb"


def longest_palindrome(strs) :
    # 뒤집어서 같거나, 한자리 글자면 그대로 리턴
    if strs == strs[::-1] or len(strs) < 2 :
        return strs

    def expand(left: int, right: int) -> str:
        # left는 0보다 커야하고, right는 최대 길이보다는 작아야한다.
        # 한자리 일 때 left와 right는 각각 i, i+1이다.
        # 두자리 일 때 left와 right는 각각 i, i+2이다.
        # 따라서, left == right-1 의 의미는
        # 한자리 일 때 그 글자가 같은지 (당연히 맞음)
        # 두자리 일 때 두 글자가 같은지 (짝수일 경우도 판별해야하므로)
        while left >= 0 and right <= len(strs) and strs[left] == strs[right-1]:
            left -= 1
            right += 1
        # 최종 비교를 위해 -1, +1 을 했으므로 리턴할 경우에는 +1, -1 을 해준다.
        return strs[left+1:right-1]

    # for 문을 돌면서 계속 이동시키면서 판별하므로,
    # 각 포인트의 결과 최대값을 기존 최대값과 비교하면서 교체해준다.
    result = ''
    for i in range(len(strs)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)

    return result


print(longest_palindrome(input1))