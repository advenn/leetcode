class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        import string

        letters = string.ascii_uppercase
        excel_letters = columnTitle
        summ = 0
        length = len(excel_letters)
        for index, letter in enumerate(excel_letters):
            summ += (letters.index(letter) + 1) * (26 ** (length - index - 1))
        return summ


s = Solution()
print(s.titleToNumber("ZY"))
# A = 1
# Z = 26 =>
# Y = 25
# ZY => 701 => Z * 26 + y => 26 * (26 ** 1) + 25 * (26 ** 0)
# AZY => A * (26 ** 2) + Z * (26 ** 1) + Y * (26 ** 0)
