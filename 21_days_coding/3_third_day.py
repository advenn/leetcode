from typing import List


class Solution:
    def searchRange_new(self, nums: List[int], target: int) -> List[int]:
        """
        this solution beat 100 % of solutions on memory usage
        link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/939124299/
        """
        if target in nums:
            length = len(nums)
            first_index = nums.index(target)
            second_index = nums[::-1].index(target)
            result = [first_index, length - 1 - second_index]
            return result
        return [-1, -1]

    def searchRange_old(self, nums: List[int], target: int) -> List[int]:
        import numpy as np

        indexes = np.where(np.array(nums) == target)
        if indexes[0].shape[0] > 0:
            indexes_ = indexes[0].tolist()
            return [indexes_[0], indexes_[-1]]
        else:
            return [-1, -1]

s = Solution()
print(s.searchRange_new([1,2,3,4], 3))
