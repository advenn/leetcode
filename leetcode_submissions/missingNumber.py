from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_ = max(nums)
        print(max_)
        for i in range(0, len(nums) + 1):
            if i not in nums:
                return i


s = Solution()
print(s.missingNumber([0, 1]))
