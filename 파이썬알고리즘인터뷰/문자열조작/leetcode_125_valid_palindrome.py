# 팰린드롬이란,
# 앞뒤가 똑같은 단어나 문장이다. 즉, 뒤집어도 똑같은 단어, 또는 문장을 말한다.
# 우리나라말로는 회문이라고도 하며 대표적으로 소주 만병만 주소 등이 있다.

# 팰린드롬인지 확인하고, 맞으면 True / 아니면 False를 출력하시오.

# 예제1. 입력 / 출력
# "A man, A plan, a canal: Panama"  /  True

# 예제2. 입력 / 출력
# "race a car"  /  False


ex1 = "A man, A plan, a canal: Panama"
ex2 = "race a car"

def check_valid_palindrome(example) :
    strs = []
    for s in example:
        if s.isalnum():
            strs.append(s.lower())

    result = "".join(strs)

    return strs == strs[::-1]

print(check_valid_palindrome(ex1))
print(check_valid_palindrome(ex2))