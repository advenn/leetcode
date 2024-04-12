from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        I suppose it's my first hard problem,
        let's solve this with in the most basic way
        it failed. will try later
        """

        for i in range(1, max(nums + [1]) + 2):
            if i not in nums:
                return i


s = Solution()
tc1 = [1, 2, 0]
tc2 = [3, 4, -1, 1]
tc3 = [7, 8, 9, 11, 12]
tc1a = 3
tc2a = 2
tc3a = 1
print(s.firstMissingPositive([-5]))
