from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate_permutations(nums, current_permutation, used_nums, result):
            if len(current_permutation) == len(nums):
                result.append(current_permutation.copy())
                return

            for num in nums:
                if num not in used_nums:
                    # // Add the current number to the permutation
                    current_permutation.append(num)
                    used_nums.add(num)

                    # // Recurse
                    generate_permutations(nums, current_permutation, used_nums, result)

                    # // Backtrack
                    current_permutation.pop()
                    used_nums.remove(num)

        def permute_(nums):
            result = []
            generate_permutations(nums, [], set(), result)
            return result

        return permute_(nums)


s = Solution()
print(s.permute([1, 2, 3]))
