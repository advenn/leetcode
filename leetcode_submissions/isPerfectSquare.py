"""
easy
https://leetcode.com/problems/valid-perfect-square/
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        squared = math.sqrt(num)
        return  int(squared) == float(squared)