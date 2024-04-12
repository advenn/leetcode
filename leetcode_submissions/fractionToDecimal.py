# from icecream import ic
#
#
# class Solution:
#     def fractionToDecimal_old(self, numerator: int, denominator: int) -> str:
#         """
#         1. numerator dan denominator ni
#         """
#         if numerator % denominator == 0:
#             return str(numerator // denominator)
#         res = ""
#         whole_part = numerator // denominator
#         numerator = numerator % denominator
#         decimal_fraction = ""
#         recurring_fraction = ""
#         seen_nums: dict[int, int] = {}
#         div, mod = numerator // denominator, numerator % denominator
#
#         while mod != 0:
#             ic(mod, div, denominator)
#             while mod < denominator:
#                 mod *= 10
#             ic(mod)
#             div, mod = div // denominator, div % denominator
#             if mod not in seen_nums.keys():
#                 seen_nums[mod] = div
#             else:
#                 break
#         ic(div, mod, seen_nums)
#
#     def fractionToDecimal(self, numerator: int, denominator: int) -> str:
#         """
#         Example 1:
#         Input: numerator = 1, denominator = 2
#         Output: "0.5"
#
#         Example 2:
#         Input: numerator = 2, denominator = 1
#         Output: "2"
#
#         Example 3:
#         Input: numerator = 4, denominator = 333
#         Output: "0.(012)"
#
#         parts:
#             butun qism
#             kasr qism
#             davriy qism
#         """
#         whole_part = numerator // denominator
#         numerator = numerator % denominator
#
#         seen_numbers = []
#
#         resps = {}
#
#         while numerator not in seen_numbers:

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = False
        if numerator*denominator < 0:
            sign = True
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part = numerator // denominator
        if sign:
            integer_part = "-" + str(integer_part)
        remainder = numerator % denominator
        if remainder == 0:
            return str(integer_part)
        remainder *= 10
        remainder_list = []
        while remainder not in remainder_list:
            remainder_list.append(remainder)
            remainder = remainder % denominator
            remainder *= 10
        fraction = "".join([str(remainder_list[i] // denominator) for i in range(len(remainder_list))])
        if int(fraction[-1]) != 0:
            remainder_index = remainder_list.index(remainder)
            fraction = fraction[:remainder_index] + "(" + fraction[remainder_index:] + ")"
        else:
            fraction = fraction[:-1]
        return f"{integer_part}." + fraction


s = Solution()
print(s.fractionToDecimal(7, 15))
