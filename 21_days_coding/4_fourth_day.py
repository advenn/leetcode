from typing import List


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         """
# 		nums = [-2,1,-3,4,-1,2,1,-5,4]   => 6
# 		"""
#         maximum = min(nums)
#         length = len(nums)
#         # if length == 1:
#         #     return maximum
#         count = 0
#         while count < length:
#             c = 1
#             while c <= length - count:
#                 # print(nums[count: c + count])
#                 summ = sum(nums[count: c + count])
#                 if summ >= maximum:
#                     maximum = summ
#                 c += 1
#             count += 1
#
#         return maximum


# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
# from sys import maxint
#
#
# def maxSubArraySum(a, size):
#     max_so_far = -maxint - 1
#     max_ending_here = 0
#
#     for i in range(0, size):
#         max_ending_here = max_ending_here + a[i]
#         if (max_so_far < max_ending_here):
#             max_so_far = max_ending_here
#
#         if max_ending_here < 0:
#             max_ending_here = 0
#     return max_so_far


# Driver function to check the above function


# print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))

# This code is contributed by _Devesh Agrawal_

class Solution_easy_one:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        index = s[::-1].index(" ")
        return index


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        n=1 -> [[1]] edge case
        n=2 -> 2,1,1
        n=3 -> 3,2,2,1,1
        n=4 -> 4,3,3,2,2,1,1
        n=5 -> 5,4,4,3,3,2,2,1,1
        n=6 -> 6,5,5,4,4,3,3,2,2,1,1
        and so on...
        directions:
            * r for right
            * d for down
            * l for left
            * u for up
        """
        directions = ('r', 'd', 'l', 'u')
        steps = []
        for i in range(1, 1 + n):
            if i != n:
                steps.append(i)
                steps.append(i)
            else:
                steps.append(i)
        steps = steps[::-1]
        result = [[0 for _ in range(n)] for _ in range(n)]
        num_range = list(range(1, 1 + n * n))
        coordinate = [0, 0]
        cnt = 0
        dir_count = 0
        for count, step in enumerate(steps):
            print('step: ', step, count)
            direction = directions[(count) % 4]
            print('direction: ', direction)
            for _ in range(step):
                print("_: ", _, coordinate)
                assignee = num_range[cnt]
                result[coordinate[0]][coordinate[1]] = assignee
                print(coordinate, count, step, direction)
                if direction == 'r':
                    if coordinate[1] <= n-1:
                        coordinate[1] += 1
                elif direction == 'd':
                    coordinate[0] += 1
                elif direction == 'l':
                    coordinate[1] -= 1
                else:
                    coordinate[0] -= 1
                cnt += 1

        return result

# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         """
#         n=1 -> [[1]] edge case
#         n=2 -> 2,1,1
#         n=3 -> 3,2,2,1,1
#         n=4 -> 4,3,3,2,2,1,1
#         n=5 -> 5,4,4,3,3,2,2,1,1
#         n=6 -> 6,5,5,4,4,3,3,2,2,1,1
#         and so on...
#         directions:
#             * r for right
#             * d for down
#             * l for left
#             * u for up
#         """
#         directions = ('r', 'd', 'l', 'u')
#         steps = []
#         for i in range(1, n+1):
#             if i != n:
#                 steps.append(i)
#                 steps.append(i)
#             else:
#                 steps.append(i)
#         steps = steps[::-1]
#         result = [[0 for _ in range(n)] for _ in range(n)]
#         num_range = list(range(1, 1 + n * n))
#         coordinate = [0, 0]
#         dir_count = 0
#         for count, step in enumerate(steps):
#             direction = directions[dir_count % 4]
#             for _ in range(step):
#                 assignee = num_range[count]
#                 result[coordinate[0]][coordinate[1]] = assignee
#                 if direction == 'r':
#                     if coordinate[1] < n:
#                         coordinate[1] += 1
#                 elif direction == 'd':
#                     coordinate[0] += 1
#                 elif direction == 'l':
#                     coordinate[1] -= 1
#                 else:
#                     coordinate[0] -= 1
#                 cnt += 1
#             dir_count += 1
#
#         return result

# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         """
#         n=1 -> [[1]] edge case
#         n=2 -> 2,1,1
#         n=3 -> 3,2,2,1,1
#         n=4 -> 4,3,3,2,2,1,1
#         n=5 -> 5,4,4,3,3,2,2,1,1
#         n=6 -> 6,5,5,4,4,3,3,2,2,1,1
#         and so on...
#         directions:
#             * r for right
#             * d for down
#             * l for left
#             * u for up
#         """
#         directions = ('r', 'd', 'l', 'u')
#         steps = []
#         for i in range(1, n+1):
#             if i != n:
#                 steps.append(i)
#                 steps.append(i)
#             else:
#                 steps.append(i)
#         steps = steps[::-1]
#         result = [[0 for _ in range(n)] for _ in range(n)]
#         num_range = list(range(1, 1 + n * n))
#         coordinate = [0, 0]
#         dir_count = 0
#         for count, step in enumerate(steps):
#             direction = directions[dir_count % 4]
#             for _ in range(step):
#                 assignee = num_range[count]
#                 result[coordinate[0]][coordinate[1]] = assignee
#                 if direction == 'r':
#                     if coordinate[1] != n-1:
#                         coordinate[1] += 1
#                 elif direction == 'd':
#                     coordinate[0] += 1
#                 elif direction == 'l':
#                     coordinate[1] -= 1
#                 else:
#                     coordinate[0] -= 1
#                 count += 1
#             dir_count += 1
#
#         return result

s = Solution()
# print(s.generateMatrix(n=1))
# print(s.generateMatrix(n=2))
# print(s.generateMatrix(n=3), sep='\n')
print(*s.generateMatrix(n=4), sep='\n')
# print(s.generateMatrix(n=5))
