# 리스트 변수를 활용해서 해쉬 테이블 구현해보기
# 1. 해쉬 함수 : key % 8
# 2. 해쉬 키 생성 : hash(data)

# 8칸 배열의 해쉬테이블 생성
hash_table = list([0 for i in range(8)])


# 키 값 생성
def get_key(data):
    return hash(data)


# 해쉬테이블의 어디에 저장할지 위치 지정
def hash_function(key):
    return key % 8


# 데이터 저장하기
def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


# 데이터 읽기
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


# 저장
save_data("Dave", "01012341234")
save_data("Andy", "01023456234")
# 읽기
print(read_data("Andy"))
# 해쉬 테이블 전체 조회
print(hash_table)


