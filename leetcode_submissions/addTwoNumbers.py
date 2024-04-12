from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    """
    latest solution performed 10 percent better than the old one
    """

    def addTwoNumbers_old_sol(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
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
        num1 = int("".join([str(i) for i in nums1[::-1]]))
        num2 = int("".join([str(i) for i in nums2[::-1]]))
        result = num1 + num2
        result = [int(i) for i in str(result)]
        result = result[::-1]
        result = [ListNode(i) for i in result]
        print(result)
        for i in range(len(result) - 1):
            result[i].next = result[i + 1]
        return result[0]

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def len_list(lst: ListNode) -> int:
            length = 0
            cur = lst
            while cur is not None:
                length += 1
                cur = cur.next
            return length

        def list_to_sum(l: ListNode) -> int:
            len_list_: int = len_list(l)
            val: int = 0
            cur: ListNode = l
            for i in range(len_list_):
                val += cur.val * (10**i)
                cur = cur.next

            return val

        def sum_to_list(sum: int) -> ListNode:
            div, mod = divmod(sum, 10)
            print(div, mod)

            nl = ListNode(mod)
            last = nl
            while div > 0:
                div, mod = divmod(div, 10)
                last.next = ListNode(mod)
                last = last.next
                print(div, mod)

            return nl

        val1 = list_to_sum(l1)
        val2 = list_to_sum(l2)

        summ = val1 + val2

        return sum_to_list(summ)


lst1 = ListNode(2, ListNode(4, ListNode(3, ListNode(2, ListNode(4, ListNode(3))))))
lst2 = ListNode(5, ListNode(6, ListNode(4)))

s = Solution()
print(s.addTwoNumbers(lst1, lst2))

print(s.addTwoNumbers(ListNode(0), ListNode(0)))
