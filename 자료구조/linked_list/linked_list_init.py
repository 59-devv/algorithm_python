# 링크드 리스트 구현해보기
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


# 링크드리스트 추가 함수 만들기
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)


# 첫번째 노드
node1 = Node(1)
head = node1


# 링크드리스트에 데이터 추가하기
for index in range(2, 10):
    add(index)


# 링크드리스트 데이터 출력하기
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)