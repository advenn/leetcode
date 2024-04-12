from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        max3 = float("-inf")  # Initialize max3 to negative infinity
        stack = []  # Initialize an empty stack
        
        for i in range(n - 1, -1, -1):
            num = nums[i]
        
            # Check if the current number is greater than max3
            if num >= max3:
                max3 = num  # Update max3 if a greater number is found
            else:
                # While the stack is not empty and num is greater than the top element of the stack
                while stack and num > stack[-1]:
                    max3 = stack.pop()  # Update max3 with the popped element
        
                # Push the current number onto the stack
                stack.append(num)
        
        return False  # If no 132 pattern is found
        # left = 0
        # right = len(nums) - 1
        #
        # while right > 0 :
        #     num = nums[right]

        #
        # while left < right - 1:
        #     while mid < right:
        #         print(
        #             f"{left = }, {mid = }, {right = }, {nums[left] = }, {nums[right] = },  {nums[right] = }, {nums[left] < nums[right] < nums[mid] = } {left < mid < right = }"
        #         )
        #         if left < mid < right and nums[left] < nums[right] < nums[mid]:
        #             return True
        #         if nums[left] >= nums[right] or nums[left] >= nums[mid]:
        #             right -= 1
        #         mid += 1
        #
        #     left += 1
        #
        # return False


nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]


s = Solution()
print(s.find132pattern(nums))
