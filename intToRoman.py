class Solution:
    def intToRoman(self, num: int) -> str:
        nums = []
        strnum = str(num)
        count = 0
        while True:
            nums.append(int(str(num)[-1 - count]) * (10 ** count))
            count += 1
            if count >= len(strnum):
                break
        nums = nums[::-1]
        ROMAN = ''
        count = 0
        while True:
            number = nums[count]
            if 4000 > number >= 1000:
                ROMAN += 'M' * int(str(number)[0])
            elif 1000 > number >= 100:
                if number == 900:
                    ROMAN += "CM"
                elif number == 500:
                    ROMAN += "D"
                elif 900 > number > 500:
                    ROMAN += "D" + ("C" * ((number - 500) // 100))
                elif number == 400:
                    ROMAN += "CD"
                else:
                    ROMAN += "C" * (number // 100)
            elif 100 > number >= 10:
                if number == 90:
                    ROMAN += "XC"
                elif number == 50:
                    ROMAN += "L"
                elif 90 > number > 50:
                    ROMAN += "L" + ("X" * ((number - 50) // 10))
                elif number == 40:
                    ROMAN += "XL"
                else:
                    ROMAN += "X" * (number // 10)
            else:
                if number == 9:
                    ROMAN += "IX"
                elif number == 5:
                    ROMAN += "V"
                elif 9 > number > 5:
                    ROMAN += "V" + ("I" * ((number - 5) // 1))
                elif number == 4:
                    ROMAN += "IV"
                else:
                    ROMAN += "I" * (number // 1)

            count += 1
            if count >= len(nums):
                break

        return ROMAN


s = Solution()
# print(s.intToRoman(3633))
# print(s.intToRoman(1542))
# print(s.intToRoman(2984))
# print(s.intToRoman(3179))
print(s.intToRoman(541))
print(s.intToRoman(58))
