"""
Well, I skip this problem, because I saw chatgpt written code
"""
class Solution:
    def isUglyMine(self, n: int) -> bool:
        """
        divide number from 2 to itself:
            if divider is not 2,3,5 then return True
        """
        if n <= 0:
            return False
        while n > 1:
            for i in range(2, n + 1):
                if n % i == 0:
                    if i not in (2, 3, 5):
                        return False
                    else:
                        n //= i
                        break

        return True

    def isUgly(self, n: int) -> bool:
        """chatgpt written code"""
        if n <= 0:
            return False

        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p

        return n == 1




s = Solution()
print(s.isUgly(-2147483648))
