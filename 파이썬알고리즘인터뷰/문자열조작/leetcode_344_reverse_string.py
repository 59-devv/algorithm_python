# 문자열 뒤집기
# 문자열을 뒤집는 함수를 작성하시오. 단, 리스트 내부를 직접 조작해야 한다.

s = ['h', 'e', 'l', 'l', 'o']
s1 = ['h', 'a', 'n', 'n', 'a', 'h']


# 1. 전통적인 방식 (two pointer)

def reverse_string1(strs) :
    left = 0
    right = len(strs)-1

    while(left < right) :
        temp = strs[left]
        strs[left] = strs[right]
        strs[right] = temp

        left += 1
        right -= 1

    return strs

print(reverse_string1(s))
print(reverse_string1(s1))

# 2. 파이썬 방식

def reverse_string2(strs) :
    return strs.reverse()

reverse_string2(s)
reverse_string2(s1)
print(s)
print(s1)