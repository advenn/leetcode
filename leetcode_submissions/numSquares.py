class Solution:
    def numSquares(self, n: int) -> int:
        ...

    def numSquaresDyn(self, n: int) -> int:
        """
        perfect squares are:
        1,4,9,16, ...

        Example 1:
        Input: n = 12
            Output: 3
            Explanation: 12 = 4 + 4 + 4.

        Example 2:
        Input: n = 13
            Output: 2
            Explanation: 13 = 4 + 9.
        """

        if n < 2:
            return n

        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        print(dp)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
                print(
                    i,
                    j,
                    dp,
                )
        return int(dp[n])

    def numSquares_(self, n: int) -> int:
        def checkAnswer(num: int) -> bool:
            sqrt_num = int(num**0.5)
            return num == sqrt_num * sqrt_num

        if checkAnswer(n):
            return 1

        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4

        for i in range(1, int(n**0.5) + 1):
            if checkAnswer(n - i * i):
                return 2

        return 3


s = Solution()
print(s.numSquares(12))
