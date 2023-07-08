from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        n = 2 -> 2:
            1. 1 step + 1 step
            2. 2 steps
        n = 3 -> 3:
            1. 1 step + 1 step + 1 step
            2. 1 step + 2 steps
            3. 2 steps + 1 step
        n = 4 -> x -> 5:
            1. 1,1,1,1
            2. 2,1,1
            3. 1,2,1
            4. 1,1,2
            5. 2,2
        n = 5 -> x -> 8:
            1. 1,1,1,1,1
            2. 2,1,1,1
            3. 1,2,1,1
            4. 1,1,2,1
            5. 1,1,1,2
            6. 2,2,1
            7. 2,1,2
            8. 1,2,2
        n = 6 -> x:
            1. 1,1,1,1,1,1
            2. 2,1,1,1,1
            3. 1,2,1,1,1
            4. 1,1,2,1,1
            5. 1,1,1,2,1
            6. 1,1,1,1,2
            7. 2,2,1,1
            8.
        '''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        c = {v: k for k, v in c.items()}
        return c[1]
