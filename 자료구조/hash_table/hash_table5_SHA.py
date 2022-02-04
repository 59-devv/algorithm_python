import hashlib

# SHA-1 실습
# hashlib 라이브러리를 먼저 import 한다.

# 아래 두 코드는 동일하다. (바이트 코드로 만들어주는 것이다.)
# data = b'test'
data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
# 16진수로 추출한다.
hex_dig = hash_object.hexdigest()
print(hex_dig)


# SHA-256 실습
data2 = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(data2)
# 16진수로 추출한다.
hex_dig = hash_object.hexdigest()
print(hex_dig)


# 앞에서 실습했던 Chaning 실습에서, key생성 함수를 SHA256으로 바꿔보기
hash_table = list([0 for i in range(8)])


def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    # 실제로 변환된 값은 문자열의 형태이고, 16진수이기 때문에
    # key로 사용하기 위해서는 10진수의 숫자로 변경해주어야 한다.
    return int(hex_dig, 16)


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # 해쉬 테이블의 기본값을 모두 0으로 설정해두었고,
    # 들어오는 값은 0이 아니라는 가정
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] == value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]

    hash_table[hash_address] = value


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None



