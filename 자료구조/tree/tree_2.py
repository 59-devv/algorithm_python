# 파이썬 객체지향 방법으로 클래스 구현해보기 (링크드 리스트)
import random
import time


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 이진탐색트리 조건에 부합하도록 데이터를 넣어야 사용할 수 있음
class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right

        return False

    def delete(self, value):
        # value가 있는지부터 확인해야한다.
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if not searched:
            return False

        # 이후부터 Case들을 분리해서 코드를 작성한다.
        # CASE1. 삭제할 Node가 Leaf Node인 경우
        if self.current_node.left is None and self.current_node.right is None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        # CASE2. 삭제할 Node가 Child Node를 한 개 가지고 있을 경우
        # Child Node가 왼쪽에 있을 경우
        elif self.current_node.left is not None and self.current_node.right is None:
            # 삭제할 Node가 좌측일 경우
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            # 삭제할 Node가 우측일 경우
            else:
                self.parent.right = self.current_node.left
        # Child Node가 우측에 있을 경우
        elif self.current_node.right is not None and self.current_node.left is None:
            # 삭제할 Node가 좌측일 경우
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            # 삭제할 Node가 우측일 경우
            else:
                self.parent.right = self.current_node.right

        # CASE3. 삭제할 Node가 Child Node를 두 개 가지고 있을 경우
        # 삭제할 Node의 우측 자식 중, 가장 작은 값으로 본인을 대체한다.
        elif self.current_node.left is not None and self.current_node.right is not None:
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left is not None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right is not None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left is not None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right is not None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

        return True


"""
이진트리에서 데이터 삭제
* leaf node 삭제: 데이터 삭제 후, parent의 branch를 None으로
* child node가 1개 있을 때: 삭제 후, child node를 parent node로 연결
* child node가 2개 있을 때: 아래 순서대로
    (1) 삭제할 Node의 오른쪽 자식 선택
    (2) 오른쪽 자식의 가장 하단, 왼쪽에 있는 node를 본인의 자리에 둔다.(가장 작은 node)
    (3) 자리를 바꾸면서, 삭제할 node와 연결된 좌측, 우측 branch도 바꿔준다.
    (3) 만약 가장 작았던 Node가 오른쪽에 값을 가지고 있었다면, 그 parent node의 좌측 branch로 연결시켜준다.
"""


# 1~999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력 / 검색 / 삭제

# 100개 숫자 랜덤 선택
bst_nums = set()

while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))

# 100개의 선택된 숫자를 이진 탐색 트리에 입력.
# 임의로 루트 노드는 500이라고 설정한다.
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 입력한 100개의 숫자 검색
for num in bst_nums:
    if not binary_tree.search(num):
        print("잘못만들었어!")

# 입력한 100개의 숫자 중 10개를 선택해서 삭제함
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자를 삭제 (삭제 가능 확인)
for del_num in delete_nums:
    if not binary_tree.delete(del_num):
        print(f"{del_num}삭제안됨/잘못만들었어!222")
