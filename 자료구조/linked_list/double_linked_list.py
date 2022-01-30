# 무조건 앞에서만 뒷 값을 찾을 수 있었던 링크드리스트의 단점을 보완하기 위해
# 뒤에서도 앞의 값을 찾을 수 있도록 만들어진 것이 더블 링크드리스트이다.
class Node:
    # 초기화
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class NodeManagement:
    def __init__(self, data):
        self.head = Node(data)
        # 뒤에서도 앞으로 검색할 수 있기 때문에, tail도 만들어준다.
        self.tail = self.head

    # 가장 뒤에 값 추가하기
    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next

            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    # 특정 데이터 앞에 값 추가하기
    def insert_before(self, new_data, target_data):
        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data is not target_data:
                node = node.prev
                if node is None:
                    # 찾는 값이 없으면
                    print("해당 값을 가진 노드가 없습니다.")
                    return False

            new = Node(new_data)
            temp = node.prev
            temp.next = new
            new.next = node
            new.prev = temp
            node.prev = new

    # 특정 데이터 뒤에 값 추가하기
    def insert_after(self, new_data, target_data):
        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data is not target_data:
                node = node.next
                if node is None:
                    # 찾는 값이 없으면
                    print("해당 값을 가진 노드가 없습니다.")
                    return False

            new = Node(new_data)
            temp = node.next
            node.next = new
            temp.prev = new
            new.next = temp
            new.prev = node

    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # 앞에서부터 데이터 검색
    def search_from_head(self, data):
        if self.head is None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

        print("해당 값을 가진 노드가 없습니다.")
        return False

    # 뒤에서부터 데이터 검색
    def search_from_tail(self, data):
        if self.head is None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev

        print("해당 값을 가진 노드가 없습니다.")
        return False


double_linked_list = NodeManagement(0)
for data in range(1, 10):
    double_linked_list.insert(data)

double_linked_list.print()
print("-----------")

# 앞에서부터 값 찾고 출력해보기
print("노드의 주소 : ", double_linked_list.search_from_head(3))
print("노드의 Data : ", double_linked_list.search_from_head(3).data)
print("-----------")

# 없는 값 찾아보기
double_linked_list.search_from_head(10)
print("-----------")

# 뒤에서부터 값 찾고 출력해보기
print("노드의 주소 : ", double_linked_list.search_from_tail(3))
print("노드의 Data : ", double_linked_list.search_from_tail(3).data)
print("-----------")

# 3 앞에 2.5를 넣어보자.
double_linked_list.insert_before(2.5, 3)
double_linked_list.print()

# 5 뒤에 5.5를 넣어보자.
double_linked_list.insert_after(5.5, 5)
double_linked_list.print()
