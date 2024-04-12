class Solution:
    def mySqrt(self, x: int) -> int:
        """

        :param x:
        :return:
        """
        if x == 1:
            return 1
        if x == 0:
            return 0
        num: int = x
        root = x / 2
        eps = 0.0000000000000001

        while (root - num / root) > eps:
            print(root, num, num / root)
            root = 0.5 * (root + num / root)

        return int(root)


s = Solution()
print(s.mySqrt(90000))
