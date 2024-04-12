# from typing import List
#
# #
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         length = len(nums)
#         count = 0
#         junk = " "
#         for i in range(1, length):
#             # print(i)
#             if nums[i - 1] != nums[i]:
#                 count += 1
#         return count + 1
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         iterating = True
#         i = 1
#
#         while iterating:
#             if i < len(nums):
#                 if nums[i - 1] == nums[i]:
#                     nums.pop(i - 1)
#                 else:
#                     i += 1
#             else:
#                 iterating = False
#         # print(nums)
#         return len(nums)
#
# s = Solution()
# print(s.removeDuplicates([1, 1, 1, 2]))
# print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
