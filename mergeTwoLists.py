from typing import Optional




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        from typing import List
        # array to linked list
        def array_to_linked_list(arr: List[int]) -> ListNode:
            if not arr:
                return []
            head = ListNode(arr[0])
            node = head
            for i in range(1, len(arr)):
                node.next = ListNode(arr[i])
                node = node.next
            return head

        # linked list to array
        def linked_list_to_array(head: ListNode) -> List[int]:
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr

        lst1 = linked_list_to_array(list1)
        lst2 = linked_list_to_array(list2)

        res = []
        while True:
            lower = 0
            if lst1[0] > lst2[0]:
                lower = lst2[0]
                res.append(lower)
                lst2.pop(0)
            else:
                lower = lst1[0]
                res.append(lower)
                lst1.pop(0)
            if not lst1 and not lst2:






# import random
# from typing import Optional, List
#
#
# def quicksort(array):
#     # print(array)
#     if len(array) < 2:
#         return array  # Base case: arrays with 0 or 1 element are already “sorted.”
#     else:
#         pivot = array[0]  # Recursive case
#         less = [i for i in array[1:] if i <= pivot]  # Sub-array of all the elements less than the pivot
#         greater = [i for i in array[1:] if i > pivot]  # Sub-array of all the elements greater than the pivot
#         return quicksort(less) + [pivot] + quicksort(greater)
#
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def mergeTwoArrays(self, list1: Optional[List], list2: Optional[List]) -> Optional[List]:
#         if not list1:
#             return list2
#         if not list2:
#             return list1
#         if list1[0] < list2[0]:
#             return [list1[0]] + self.mergeTwoArrays(list1[1:], list2)
#         else:
#             return [list2[0]] + self.mergeTwoArrays(list1, list2[1:])
#
#
# # class Solution:
# #     def mergeTwoLists(self, list1: Optional[List], list2: Optional[List]) -> Optional[List]:
# #         """
# #         merge two arrays in ascending order
# #         """
# #         if not list1:
# #             return list2
# #         if not list2:
# #             return list1
# #         if not list1 and list2:
# #             return []
# #         vals = []
# #         while True:
# #             # print(vals)
# #             if list1 == [] and list2:
# #                 vals.append(list2.pop(0))
# #             elif list2 == [] and list1:
# #                 vals.append(list1.pop(0))
# #             elif not list1 and not list2:
# #                 return vals
# #             elif list1[0] >= list2[0]:
# #                 vals.append(list2.pop(0))
# #             elif list2[0] >= list1[0]:
# #                 vals.append(list1.pop(0))
#
#
# lst1 = quicksort([random.randint(1, 1000) for _ in range(10)])
# lst2 = quicksort([random.randint(1, 1000) for _ in range(10)])
# print(lst1, lst2, sep="\n")
# s = Solution()
# print(s.mergeTwoArrays(
#     list1=lst1,
#     list2=lst2
# ))
#
#
# # while True:
# #     if not list1:
# #         return list2
# #     if not list2:
# #         return list1
# #     if list1[0] < list2[0]:
# #         vals.append(list2.pop(0))
# #         if not list2:
# #             return list1
# #     else:
# #         vals.append(list1.pop(0))
# #         if not list1:
# #             return list2
# # return list1 + list2
# #
#
#
# # array to linked list
# def array_to_linked_list(arr: List[int]) -> ListNode:
#     if not arr:
#         return None
#     head = ListNode(arr[0])
#     node = head
#     for i in range(1, len(arr)):
#         node.next = ListNode(arr[i])
#         node = node.next
#     return head
#
#
# # linked list to array
# def linked_list_to_array(head: ListNode) -> List[int]:
#     arr = []
#     while head:
#         arr.append(head.val)
#         head = head.next
#     return arr
#
#
# print(linked_list_to_array(array_to_linked_list([1, 2, 3, 4, 5])))
# print(array_to_linked_list([1, 2, 3, 4, 5]))
