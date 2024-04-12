# #!/usr/bin/env python
# import decimal
#
#
# def sqrt(n):
#     assert n > 0
#     with decimal.localcontext() as ctx:
#         ctx.prec += 2  # increase precision to minimize round off error
#         x, prior = decimal.Decimal(n), None
#         while x != prior:
#             prior = x
#             x = (x + n / x) / 2  # quadratic convergence
#     return +x  # round in a global context
#
#
# decimal.getcontext().prec = 80  # desirable precision
# r = sqrt(12345)
# print(r)
# print(r == decimal.Decimal(12345).sqrt())
from icecream import ic


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        isMinus = n < 0
        n = abs(n)
        result = 1
        while n > 1:
            if n % 2 == 0:
                x *= x
                n //= 2
            else:
                result *= x
                n -= 1
        result *= x
        if isMinus:
            return 1 / result
        return result


s = Solution()
print(s.myPow(2.0000, 10))
# print(s.myPow(3.0, 5))
