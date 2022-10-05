from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        from math import log10
        length = len(digits) - 1
        print(length)
        lst1 = []
        for i in range(length, 0 - 1, -1):
            lst1.append(digits[abs(i - length)] * (10 ** abs(i)))
        lst1.append(1)
        # print(lst1)
        summ = sum(lst1)
        lst2 = []
        length = int(log10(summ))
        for i in range(length + 1):
            if i != length:
                appendee = summ // (10 ** abs(i - length))
                lst2.append(appendee)
                summ -= appendee * (10 ** abs(i - length))
            else:
                lst2.append(summ)
        return lst2


s = Solution()
print(s.plusOne([4, 3, 2, 1]))
print(s.plusOne([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))
print(s.plusOne([1, 2, 3]))
print(s.plusOne([1, 2, 9]))
print(s.plusOne([9]))
print(s.plusOne([1, 0, 0, 0, 0]))
