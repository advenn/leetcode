from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0

        pass







s = Solution()
print(s.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
print(s.threeSumClosest(nums=[0, 2, 1, -3], target=1))
print(s.threeSumClosest(nums=[1, 1, 1, 0], target=-100))
