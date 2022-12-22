from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = []
        nums2 = []
        while True:
            nums1.append(l1.val)
            l1 = l1.next
            if l1 is None:
                break

        while True:
            nums2.append(l2.val)
            l2 = l2.next
            if l2 is None:
                break
        num1 = int(''.join([str(i) for i in nums1[::-1]]))
        num2 = int(''.join([str(i) for i in nums2[::-1]]))
        result = num1 + num2
        result = [int(i) for i in str(result)]
        result = result[::-1]
        result = [ListNode(i) for i in result]
        print(result)
        for i in range(len(result)-1):
            result[i].next = result[i+1]
        return result[0]



lst1 = ListNode(2, ListNode(4, ListNode(3)))
lst2 = ListNode(5, ListNode(6, ListNode(4)))

s = Solution()
print(s.addTwoNumbers(lst1, lst2).val)