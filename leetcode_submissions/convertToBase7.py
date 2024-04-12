class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        15 in 7 = 21
        15 % 7 = 1
        15 // 7 = 2
        1 % 7 = 1
        1 // 7 = 0



        100 in 7 = 202
        100 % 7 = 2
        100 // 7 = 12
        12 & 7 = 5
        12 // 7 = 1
        5 % 7 = 5
        """