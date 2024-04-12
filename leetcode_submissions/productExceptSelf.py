from typing import List

from icecream import ic


#
#
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         has_zero = True if 0 in nums else False
#         product = 1
#         cnt = 0
#         for i in nums:
#             if i != 0:
#                 product *= i
#                 cnt += 1
#         if len(nums) - cnt > 1:
#             product = 0
#         for index, value in enumerate(nums):
#             if has_zero:
#                 if value != 0:
#                     nums[index] = 0
#                 else:
#                     nums[index] = product
#             else:
#                 nums[index] = product // nums[index]
#         return nums
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0] * n
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        return result


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
