class Solution:
    def reverse(self, x: int) -> int:
        left_edge = -2 ** 31
        right_edge = 2 ** 31 - 1
        if x < 0:
            negative = True
        else:
            negative = False
        reversed = int(str((abs(x)))[::-1])
        if negative:
            reversed= 0 - reversed
        if left_edge < reversed < right_edge:
            return reversed
        else:
            return 0


s = Solution()
print(s.reverse(-123))
