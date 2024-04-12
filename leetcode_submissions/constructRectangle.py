"""
easy one: https://leetcode.com/problems/construct-the-rectangle/description/
not efficient
"""
import math
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        half = int(math.sqrt(area))
        L = half
        W = half
        while True:
            while W > 0:
                multiplied = L * W
                if multiplied == area:
                    return [L, W]
                if multiplied < area:
                    L += 1
                else:
                    break
            W -= 1


s = Solution()
print(s.constructRectangle(122122))
