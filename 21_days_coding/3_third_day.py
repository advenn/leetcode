from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            length = len(nums)
            first_index = nums.index(target)
            second_index = nums[::-1].index(target)
            result = [first_index, length - 1 - second_index]
            return result
        return [-1, -1]


s = Solution()
print(s.searchRange([1], 1))
