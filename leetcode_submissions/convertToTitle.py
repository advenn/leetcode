class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        701 = ZY => 701 // 26 + 25
        >>> divmod(701,26)
        (26, 25)   -> ZY
        >>> divmod(25,26)
        (0, 25)   -> Y
        """
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, mod = divmod(columnNumber, 26)
            result = letters[mod] + result
        return result


s = Solution()
print(s.convertToTitle(701))
