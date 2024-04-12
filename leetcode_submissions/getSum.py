class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        implement add operator without using + or -
        :param a:
        :param b:
        :return:
        """
        # x, y = a, b
        # while y != 0:
        #     carry = x & y
        #     x = x ^ y
        #     y = carry << 1
        #
        # return x
        return sum([a, b])


s = Solution()
print(s.getSum(1, 2))
print(s.getSum(-2, 3))
print(s.getSum(12, 36))
# print(7 | 2)
