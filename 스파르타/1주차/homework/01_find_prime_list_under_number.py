input = 20

# 소수 찾기

# 소수는 자기 자신과 1 외에는 어떤 수로도 나누어 떨어지지 않는다.
# N의 제곱근보다 크지 않은 어떤 소수로도 나누어지지 않는다.
def find_prime_list_under_number(number):
    # 소수 리스트를 만드다.
    prime_list = []

    for n in range(2, number + 1):
        # 해당 수가 소수로 나누어 떨어지면 안되므로, 소수 리스트에서만 값을 나누어본다.
        for i in prime_list:
            # n의 제곱근보다 크지 않은 어떤 소수로도 나누어지지 않으므로,
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)