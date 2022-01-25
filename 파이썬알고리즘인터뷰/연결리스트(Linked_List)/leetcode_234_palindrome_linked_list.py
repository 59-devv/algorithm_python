# 연결리스트가 팰린드롬 구조인지 판별하시오.

# 예제1
import collections
from typing import Optional, List, Deque

head1 = [1, 2]
output1 = False

# 예제2
head2 = [1, 2, 2, 1]
output2 = True


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(head1)
node2 = ListNode(head2)

# 풀이 1. 리스트에 값을 넣어서 확인하기
def is_palindrome_by_list(head: ListNode) -> bool:
    headList: List = []

    if not head:
        return True

    node = head
    while node is not None:
        headList.append(node.val)
        node = node.next

    while len(headList[0]) > 1:
        if headList[0].pop(0) != headList[0].pop():
            return False

    return True

# 풀이 2. deque 이용하기
def is_palindrome_by_deque(head: ListNode) -> bool:
    headList: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        headList.append(node.val)
        node = node.next

    while len(headList) > 1:
        if headList.popleft() != headList.pop():
            return False

    return True

print(is_palindrome_by_deque(node1))
print(is_palindrome_by_deque(node2))
