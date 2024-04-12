# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")  # To indicate the end of the list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        print_linked_list(cur)
        prev = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)
s = Solution()
print(s.reverseList(head))
