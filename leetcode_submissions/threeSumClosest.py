from typing import List


# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         """
#         this is really similar to 3Sum problem, so I try to use that solution here
#         I used quicksort algorithm on 3Sum, recently I read that timsort is more stable
#         than quicksort, and python's builtin `sorted` function uses timsort algorithm.
#         so I am going to use `sorted` (`timsort`) on sorting cases
#         """
#
#         import math
#         def search(numbers: list, third: int):
#             if not numbers:
#                 return []
#             if len(numbers) == 1:
#                 return numbers
#             closest1 = abs(numbers[0])
#             answers = []
#             for elem in numbers:
#                 diff1 = abs(third - elem)
#                 if diff1 <= closest1:
#                     answers.append(elem)
#                     closest1 = elem
#             return answers
#
#         length = len(nums)
#         nums = sorted(nums)
#         closest = math.inf
#         dist_to_target = math.inf
#         for i in range(length):
#             for j in range(i + 1, length):
#                 two_sum = nums[i] + nums[j]
#                 third = target - two_sum
#                 need_numbers = search(nums[(j + 1):], third)
#                 if not need_numbers:
#                     continue
#                 for nm in need_numbers:
#                     three_sum = two_sum + nm
#                     print(three_sum == - 2805, nums[i], nums[j], nm)
#                     diff = abs(target - three_sum)
#                     print(need_numbers, diff, three_sum, dist_to_target, closest)
#                     if diff <= dist_to_target:
#                         dist_to_target = diff
#                         closest = three_sum
#         return closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        closest_sum = float("inf")  # Set an initial value to infinity
        closest_diff = float("inf")  # Set an initial value to infinity

        for i in range(length - 2):
            left, right = i + 1, length - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(target - current_sum)

                if current_diff < closest_diff:
                    closest_sum = current_sum
                    closest_diff = current_diff

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum


nums = [-1, 2, 1, -4]
target = 1

s = Solution()
nums = [
    13,
    252,
    -87,
    -431,
    -148,
    387,
    -290,
    572,
    -311,
    -721,
    222,
    673,
    538,
    919,
    483,
    -128,
    -518,
    7,
    -36,
    -840,
    233,
    -184,
    -541,
    522,
    -162,
    127,
    -935,
    -397,
    761,
    903,
    -217,
    543,
    906,
    -503,
    -826,
    -342,
    599,
    -726,
    960,
    -235,
    436,
    -91,
    -511,
    -793,
    -658,
    -143,
    -524,
    -609,
    -728,
    -734,
    273,
    -19,
    -10,
    630,
    -294,
    -453,
    149,
    -581,
    -405,
    984,
    154,
    -968,
    623,
    -631,
    384,
    -825,
    308,
    779,
    -7,
    617,
    221,
    394,
    151,
    -282,
    472,
    332,
    -5,
    -509,
    611,
    -116,
    113,
    672,
    -497,
    -182,
    307,
    -592,
    925,
    766,
    -62,
    237,
    -8,
    789,
    318,
    -314,
    -792,
    -632,
    -781,
    375,
    939,
    -304,
    -149,
    544,
    -742,
    663,
    484,
    802,
    616,
    501,
    -269,
    -458,
    -763,
    -950,
    -390,
    -816,
    683,
    -219,
    381,
    478,
    -129,
    602,
    -931,
    128,
    502,
    508,
    -565,
    -243,
    -695,
    -943,
    -987,
    -692,
    346,
    -13,
    -225,
    -740,
    -441,
    -112,
    658,
    855,
    -531,
    542,
    839,
    795,
    -664,
    404,
    -844,
    -164,
    -709,
    167,
    953,
    -941,
    -848,
    211,
    -75,
    792,
    -208,
    569,
    -647,
    -714,
    -76,
    -603,
    -852,
    -665,
    -897,
    -627,
    123,
    -177,
    -35,
    -519,
    -241,
    -711,
    -74,
    420,
    -2,
    -101,
    715,
    708,
    256,
    -307,
    466,
    -602,
    -636,
    990,
    857,
    70,
    590,
    -4,
    610,
    -151,
    196,
    -981,
    385,
    -689,
    -617,
    827,
    360,
    -959,
    -289,
    620,
    933,
    -522,
    597,
    -667,
    -882,
    524,
    181,
    -854,
    275,
    -600,
    453,
    -942,
    134,
]
target = -2805

print(s.threeSumClosest(nums=nums, target=target) == target)
# mine: -2807
# correct: -2805

print(s.threeSumClosest(nums=[0, 2, 1, -3], target=1))
print(s.threeSumClosest(nums=[1, 1, 1, 0], target=-100))
print(s.threeSumClosest(nums=[-100, -98, -2, -1], target=-101))

# def search(numbers: list, third: int):
#     closest1 = abs(numbers[1])
#     answers = []
#     for elem in numbers:
#         diff1 = abs(third - elem)
#         if diff1 <= closest1:
#             answers.append(elem)
#             closest1 = elem
#     return answers
#
#
# print(search([-1, 2, 1, -4], 1))
