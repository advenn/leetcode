from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def quicksort(array):
            # print(array)
            if len(array) < 2:
                return (
                    array  # Base case: arrays with 0 or 1 element are already “sorted.”
                )
            else:
                pivot = array[0]  # Recursive case
                less = [
                    i for i in array[1:] if i <= pivot
                ]  # Sub-array of all the elements less than the pivot
                greater = [
                    i for i in array[1:] if i > pivot
                ]  # Sub-array of all the elements greater than the pivot
                return quicksort(less) + [pivot] + quicksort(greater)

        nums = quicksort(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]


s = Solution()
print(s.findDuplicate([3, 1, 3, 4, 2]))
