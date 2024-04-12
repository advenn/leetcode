class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        s = (a1 + an) * n / 2 -> n_given = (1 +
        """

        def solve_quadratic_equation(a=1, b=1, c: int = 0) -> float or int:
            """
            The equation: n * n + n - c = 0
            """
            dis_form = b * b + 4 * a * c
            import math

            sqrt_val = math.sqrt(abs(dis_form))
            if dis_form > 0:
                s1 = (-b + sqrt_val) / (2 * a)
                s2 = (-b - sqrt_val) / (2 * a)
                return max(s1, s2)
            elif dis_form == 0:
                s1 = -b / (2 * a)
                return s1

        return int(solve_quadratic_equation(c = 2 * n))


s = Solution()
print(s.arrangeCoins(5))
