from icecream import ic


class Solution:
    def solve(self, k, target):
        ic(target, 1 + k, (target % (1 + k)), (target % (1 + k)) != 0)
        return (target % (1 + k)) != 0


s = Solution()
s.solve(2, 9)
