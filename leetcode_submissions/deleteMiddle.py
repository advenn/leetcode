# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        def get_length(l: ListNode) -> int:
            count = 1
            cur = l
            while cur.next is not None:
                count += 1
                cur = cur.next
            return count

        llist_length = get_length(head)
        to_drop = llist_length // 2 + 1
        count = 1
        cur = head
        while count <= to_drop:
            if count == to_drop - 1:
                if cur.next is not None:
                    cur.next = cur.next.next
            if cur.next is not None:
                cur = cur.next
            count += 1
        return head


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")  # To indicate the end of the list


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)
s = Solution()
print_linked_list(head)
ren = s.deleteMiddle(head)
print_linked_list(ren)
