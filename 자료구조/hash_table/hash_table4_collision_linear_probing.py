# Linear Probing 기법으로 충돌 해결해보기
import hashlib

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
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] == value
                return
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None

