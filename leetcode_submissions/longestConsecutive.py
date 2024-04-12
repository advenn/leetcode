from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        I think, at first, array must be sorted, I prefer sorted() built-in method,
        because it is more optimized, it has lower O(n* log(n))
        after sorting I am going to use linear approach.
        parameters:
            longest_consecutive: int
            current_index: int
            left_elements: int = len(nums) - index
        we start from 0 till the end
        """
        if not nums:
            return 0
        nums = sorted(set(nums))
        # print(nums)
        longest_consecutives = []
        longest_consecutive = 1
        last_element = nums[0]
        for element in nums[1:]:
            if element - last_element == 1:
                longest_consecutive += 1
                last_element = element
            else:
                longest_consecutives.append(longest_consecutive)
                longest_consecutive = 1
                last_element = element

        return max(longest_consecutives + [longest_consecutive])


s = Solution()
tc1 = [100, 4, 200, 1, 3, 2]
tc2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
for tc in [tc1, tc2]:
    print(s.longestConsecutive(tc))
