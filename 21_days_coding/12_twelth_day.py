from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter

        cntr = Counter(nums)
        cntr = sorted(cntr.items(), key=lambda x: x[1], reverse=True)
        return cntr[0][0]


s = Solution()
print(s.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
