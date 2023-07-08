class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        def fibonacci(n: int):
            """
            return list of Fibonacci numbers lower than n
            """
            a, b = 0, 1
            fibs = []
            count = 0

            while count <= n:
                a, b = b, a + b
                fibs.append(a)
                count += 1
            return fibs[-1]

        return fibonacci(n - 1) + fibonacci(n - 2)

    def convertToTitle(self, columnNumber: int) -> str:
        from string import ascii_uppercase
        num2letter = {index + 1: letter for index, letter in enumerate(ascii_uppercase)}
        print(num2letter)



s = Solution()
print(s.convertToTitle(1))
