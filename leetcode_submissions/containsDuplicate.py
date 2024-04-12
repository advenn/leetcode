from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if num in counter.keys():
                return True
            else:
                counter[num] = 1
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
