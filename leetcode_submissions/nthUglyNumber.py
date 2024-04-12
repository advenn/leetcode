class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
        [1, 2**1, 3**1, 2**2, 5**1, 2**1*3**1
        """
        if n < 2:
            return 1
        ugly_nums = [1]

