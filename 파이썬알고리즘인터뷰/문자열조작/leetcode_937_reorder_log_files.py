# 로그를 재정렬하라. 기준은 아래와 같다.
# 1. 로그의 가장 앞 부분은 식별자다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순이다.
# 4. 숫자 로그는 입력 순서대로 한다.

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig",
        "let3 art zero"]

# 람다식을 사용해서 조건대로 정렬을 할 수 있다.
# 단, 람다식을 쓰기 이전에 두번째 부분을 기준으로 숫자/문자를 나누어야 한다.

digits = []
letters = []

for log in logs :
    if log.split()[1].isdigit():
        digits.append(log)
    else :
        letters.append(log)

# 첫번째 조건 = a.split()[1:]
# 첫번째 조건이 모두 같을 경우, 두번째 조건 = a.split()[0:]
letters.sort(key=lambda a : (a.split()[1:], a.split()[0:]))

# 정렬이 완료되었으므로, 두 배열을 붙여준다.
result = letters + digits

print(result)