from typing import List

import time

start = time.time()


class Solution:
    def threeSum(self, nums: List[int]):
        if len(nums) < 3:
            return []

        def quicksort(array):
            # print(array)
            if len(array) < 2:
                return array
            else:
                pivot = array[0]
                less = [i for i in array[1:] if i <= pivot]
                greater = [i for i in array[1:] if i > pivot]
                return quicksort(less) + [pivot] + quicksort(greater)

        length = len(nums)
        nums = quicksort(nums)
        results = []
        for i in range(length):
            for j in range(i + 1, length):
                twosum = nums[i] + nums[j]
                rev = 0 - twosum
                if rev in nums[j:]:
                    if sorted([nums[i], nums[j], rev]) not in results:
                        results.append(sorted([nums[i], nums[j], rev]))
        return results


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
