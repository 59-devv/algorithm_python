# 링크드리스트의 생성, 값 추가, 출력에 대한 함수를 모두 구현

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeManagement:
    # 가장 첫 값을 가지고 있도록 첫 값을 지정해줌
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def delete(self, data):
        # 첫번째 노드를 삭제할 경우
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
            return
        # 첫번째 노드가 아닌 경우
        else :
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

        # 없는 노드일 경우
        print("해당 값을 가진 노드가 없습니다.")
        return

    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else :
                node = node.next

        #없는 노드일 경우
        print("해당 값을 가진 노드가 없습니다.")
        return


linked_list1 = NodeManagement(0)
print(f"head of linked_list1 : {linked_list1.head}")
print("----------")

# 정상적으로 삭제되었다면 None이 출력되어야 함
linked_list1.delete(0)
print(linked_list1.head)
print("----------")

# 다시 노드에 값 넣고 값들 추가해보기
linked_list1 = NodeManagement(0)

for data in range(1, 10):
    linked_list1.add(data)

# 0~9가 출력되면 정상적으로 값이 추가되었음
linked_list1.print()
print("----------")

# 중간 값중 하나 삭제해봄
linked_list1.delete(4)
linked_list1.print()
print("----------")

# 마지막 값 삭제해봄
linked_list1.delete(9)
linked_list1.print()
print("----------")

# 없는 값을 삭제할 경우, 값이 없다는 것이 출력되어야 함
linked_list1.delete(4)
print("----------")

# 값이 3인 노드를 찾아보기
print("노드의 주소 : ",  linked_list1.search_node(3))
print("노드의 Data : ", linked_list1.search_node(3).data)
