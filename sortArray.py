from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(arr: list) -> list:
            if len(arr) < 2:
                return arr
            else:
                pivot = arr[0]
                less = [i for i in arr[1:] if i <= pivot]
                greater = [i for i in arr[1:] if i > pivot]
                return quicksort(less) + [pivot] + quicksort(greater)

        array = quicksort(nums)
        return array