# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def create_list(r: list):
#     head = ListNode(r[0])
#     cur = head
#     for i in r[1:]:
#         cur.next = ListNode(i)
#         cur = cur.next
#     return head
#
#
# def get_length(l: ListNode):
#     count = 1
#     cur = l
#     while cur.next is not None:
#         count += 1
#         cur = l.next
#     return count
#
# llist = create_list(list(range(1,6)))
# print(llist)
# # print((get_length(llist)))
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        def get_length(l: ListNode):
            count = 1
            cur = l
            while cur.next is not None:
                count += 1
                cur = cur.next
            return count

        llist_length = get_length(head)

        dummy = ListNode(0, head)

        reverse_index = llist_length - n + 1
        cur = dummy
        count = 0

        while count <= reverse_index:
            if count == reverse_index - 1:
                if cur.next is not None:
                    cur.next = cur.next.next
            if cur.next is not None:
                cur = cur.next
            count += 1

        return dummy.next


# Function to loop through a linked list and print its values
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")  # To indicate the end of the list


# Example usage:
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    # node5 = ListNode(5)
    # node4 = ListNode(4, node5)
    # node3 = ListNode(3, node4)
    node2 = ListNode(
        2,
    )
    head = ListNode(1, node2)

    # Loop through and print the linked list
    print_linked_list(head)
    s = Solution()
    ren = s.removeNthFromEnd(head, 1)
    print_linked_list(ren)
