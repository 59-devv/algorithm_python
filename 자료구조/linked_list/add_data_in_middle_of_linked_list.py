# 1, 2, 3, ... 9 의 링크드리스트에서,
# 1과 2 사이에 1.5라는 값을 넣고 싶을 때 어떻게 할까?
# 1의 포인터가 1.5를 가리키도록 변경, 1.5의 포인터가 2를 가리키도록 설정

# 링크드 리스트 구현
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


node2 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

# 현재 node.next는 1의 다음인 2에 대한 node이다.
# 이 node.next를 1.5로 바꿔준다.
node_next = node.next
node.next = node2
# node.next는 1.5로 바뀌었다. 이제 node2.next를 2에 대한 node로 변경해주면 된다.
node2.next = node_next

while node.next:
    print(node.data)
    node = node.next
print(node.data)

