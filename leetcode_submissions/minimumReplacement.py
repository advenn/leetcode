from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """
        non-decreasing order - increasing bo'lmagan,
        [3,9,3]-> [3,3,6,3] -> [3,3,3,3,3] = 2
        # [5,6,7] -> [5,2,4,7] = 1
        [1,2,3,4,5]  ->  X

        steps:
        * loop qilish:
            * agar i <= i + 1 <= i + 2 bo'lsa pass
            * aks holda i sonni ayirish va insert qilish kk

        :official hint:
        You can iterate from the second last element to the first.
        If the current value is greater than the previous bound,
        we want to break it into pieces so that
        the smaller one is as large as possible but not larger than the previous one.
        """
        overall_partitions = 0
        for i in range(len(nums) - 2, 0, -1):
            print(i)


nums = [3, 9, 3]
s = Solution()
print(s.minimumReplacement(nums))
