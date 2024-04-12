import math

from icecream import ic


class Solution:
    def bulbSwitch(self, n: int) -> int:
        # The algorithm:
        # array = [True for _ in range(n)]
        # for i in range(2, n + 1):
        #     m = n // i
        #     for j in range(1, m + 1):
        #         array[j * i - 1] = not array[j * i - 1]
        # return sum(array)

        return int(math.sqrt(n))


s = Solution()
for i in range(101):
    ans = s.bulbSwitch(i)
    ic(i, ans)
