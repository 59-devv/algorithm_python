"""
Hash Table
1. 해쉬 구조
    * Key와 Value로 구성된 자료구조
    * Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
    * 파이썬 Dictionary 타입이 Hash Table의 예
    * 보통 배열로 미리 Hash Table 사이즈 만큼 생성 후 사용
    * 단, 파이썬에서는 Dictionary를 사용하면 되므로 별도로 구현할 필요가 없다.

2. 용어
    * Hash : 임의 값을 고정 길이로 변환하는 것
    * Hash Table : 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
    * Hashing Function : Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
    * Hash Value / Hash Address : Key를 해싱 함수로 연산해서 해쉬 값을 알아내고 이를 기반으로
                                  Hash Table에서 Key에 대한 데이터 위치를 일관성 있게 찾을 수 있음
    * Slot : 한 개의 데이터를 저장할 수 있는 공간
    * 저장할 데이터에 Key를 추출할 수 있는 별도 함수도 존재할 수 있다.

3. Hash Table의 장단점
    (1) 장점
        * 데이터의 저장, 읽기 속도가 굉장히 빠르다. (검색 속도가 빠르다.)
        * 해쉬는 키에 대한 데이터가 있는지 중복 확인이 쉽다.
    (2) 단점
        * 일반적으로 저장공간이 조금 더 많이 필요하다.
        * 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요하다.
    (3) 주요 용도
        * 검색이 많이 필요한 경우
        * 저장, 삭제, 읽기가 빈번한 경우
        * 캐쉬 구현 시 (중복 확인이 쉽기 때문에 많이 사용함)

4. 충돌(Collision) 해결 알고리즘
    (1) Chaning 기법
        * 개방 해슁 또는 Open Hashing 기법 중 하나. 해쉬테이블 저장공간 외의 공간을 활용하는 기법
        * 충돌이 일어나면, 링크드리스트를 사용해서 링크드리스트로 데이터를 추가로 뒤에 연결시키는 방법
    (2) Linear Probing 기법
        * 폐쇄 해슁 또는 Close Hashing 기법 중 하나. 해쉬테이블 저장공간 안에서 충돌 문제를 해결하는 기법
        * 충돌이 일어나면 해당 Hash Address의 다음 Address 부터 맨 처음 나오는 빈 공간에 저장하는 방법

5. 충돌을 사전에 방지하는 방법
    * 해쉬 함수를 재정의하고 테이블 저장 공간을 확대한다 (저장될 것으로 예상되는 크기의 2배)

6. 해쉬 함수와 키 생성 함수
    * 파이썬의 hash() 함수는 실행할 때마다 값이 달라질 수 있다.
    * 따라서, 다른 해쉬 함수를 사용하는 것이 좋다.
    * ex) SHA (Secure Hash Algorithm)

7. 해쉬 테이블의 시간 복잡도
    (1) 일반적인 경우(Collision이 없는 경우)에는 O(1)이다.
    (2) 최악의 경우(Collision이 모두 발생하는 경우)에는 O(n)이다.
    * 해쉬 테이블의 경우 일반적인 경우를 기대하고 만들기 때문에, 시간 복잡도는 O(1)이라고 말한다.

8. 해쉬 테이블을 검색에서 사용할 때 예시
    (1) 해쉬 테이블을 사용하지 않을 때
        : 16개의 배열에 데이터를 저장하고 검색할 때 = O(n)
    (2) 해쉬 테이블을 사용할 때
        : 16개의 저장공간을 가진 해쉬 테이블에 데이터를 저장하고 검색할 때 = O(1)
"""

# 간단한 해쉬 예시
# hash table 만들기
hash_table = list([i for i in range(10)])
print(hash_table)


# hash function 만들기
# 가장 간단한 방식은 Division 방법(나누기를 통해 나머지 값을 사용하는 기법)
def hash_func(key):
    return key % 5


# hash table에 저장해보기
# 데이터에 따라 필요 시 key 생성 방법에 대한 정의가 필요함
data1 = "Andy"
data2 = "Dave"
data3 = "Trump"

## ord = 문자의 ASCII 코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), hash_func(ord(data1[0])))


# 저장 예시
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


# 전화번호를 저장해본다.
storage_data("Andy", "01012341234")
storage_data("Dave", "01022341234")
storage_data("Trump", "01032341234")


# 실제 데이터를 저장하고 읽어보기
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data("Andy"))