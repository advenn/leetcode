class Solution:
    def myAtoi(self, s: str) -> int:
        left_edge = -2 ** 31
        right_edge = 2 ** 31 - 1
        if not s:
            return 0
        number = ''
        s = s.strip()
        if s[0] not in ("-", "+", "0", '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return 0
        for i in s:
            if i in ("-", "0", '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                number += i
            # elif i == "+":
            #     pass
            else:
                break
        if not number:
            return 0
        reversed = int(number)
        if left_edge < reversed < right_edge:
            return reversed
        elif reversed < left_edge:
            return left_edge
        else:
            return right_edge







        # import re
        # num = re.findall(r'\d+', s)[0]
        # if not num:
        #     return 0
        # index = s.index(num)
        # if s[index-1] == "-":
        #     num = "-" + num
        # return int(num)



s = Solution()
print(s.myAtoi("-+12"))
print(s.myAtoi("3.14159"))
print(s.myAtoi("4193 with words"))
