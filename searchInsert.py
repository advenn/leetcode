"""
leetcode link: https://leetcode.com/problems/search-insert-position/
level: easy
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0
            while low <= high:
                mid = (high + low) // 2
                if arr[mid] < x:
                    low = mid + 1
                elif arr[mid] > x:
                    high = mid - 1
                else:
                    return mid
            return -1

        length = len(nums)
        pos = binary_search(arr=nums, x=target)
        if pos != -1:
            return pos
        index = 0
        while True:
            distance = target - nums[index]
            if distance < 0:
                return index
            index += 1
            if index >= length:
                return index


s = Solution()
# print(s.searchInsert(nums=[i + 1 for i in range(1,101,2)], target=19))
lst = [1, 3, 5, 6]
target = 7
print(lst, target, sep='\n')
print(s.searchInsert(nums=lst, target=target))
