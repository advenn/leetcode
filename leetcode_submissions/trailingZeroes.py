from icecream import ic


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        15! = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*...20*...*25*...*30
        """
        if n < 5:
            return 0
        twos = n // 2
        fives_ = 0
        for f in range(5, n + 1, 5):
            while f % 5 == 0:
                fives_ += 1
                f //= 5
        return min(twos, fives_)



s = Solution()
print(s.trailingZeroes(30))
print(s.trailingZeroes(50))
print(s.trailingZeroes(3))
print(s.trailingZeroes(5))
