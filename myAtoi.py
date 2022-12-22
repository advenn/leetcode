class Solution:
    def myAtoi(self, s: str) -> int:
        # Base condition
        if s is None or len(s) < 1:
            return 0
        # Max and Min values for the integers
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # Trimmed string
        s = s.lstrip()
        # Counter
        i = 0
        # Flag to indicate if the number is negative
        isNegative = len(s) > 1 and s[0] == '-'
        # Flag to indicate if the number is positive
        isPositive = len(s) > 1 and s[0] == '+'
        if isNegative:
            i += 1
        elif isPositive:
            i += 1
        # This will store the converted number
        number = 0
        # Loop for each numeric character in the string iff numeric characters are leading
        # characters in the string
        while i < len(s) and '0' <= s[i] <= '9':
            print('number:', number)
            number = number * 10 + (ord(s[i]) - ord('0'))
            i += 1
        # Give back the sign to the number
        if isNegative:
            number = -number
        # Edge cases - integer overflow and underflow
        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX
        return number


        # left_edge = -2 ** 31
        # right_edge = 2 ** 31 - 1
        # if not s:
        #     return 0
        # number = ''
        # s = s.strip()
        # if s[0] not in ("-", "+", "0", '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        #     return 0
        # for i in s:
        #     if i in ("-", "0", '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        #         number += i
        #     # elif i == "+":
        #     #     pass
        #     else:
        #         break
        # if not number:
        #     return 0
        # reversed = int(number)
        # if left_edge < reversed < right_edge:
        #     return reversed
        # elif reversed < left_edge:
        #     return left_edge
        # else:
        #     return right_edge







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
