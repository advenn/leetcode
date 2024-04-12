from icecream import ic

# partly correct, as far as I remember it got TL or not my memory sucks
class Solution:
    def calculate(self, s: str) -> int:
        """
        str bo'ylab loop qilish,
        1. 2nd level operatorlarni topish
            unga aloqador sonlarni olish
            amalni bajarib natijasini replace qilish
        2. 1st level operatorlarni topish
             unga aloqador sonlarni olish, (-) lik sonni tekshirish
             amalni bajarib replace qilish
        """
        s = s.replace(" ", "")
        while "*" in s or "/" in s:
            for index, value in enumerate(s):
                if value == "/":
                    start: int = 0
                    before: str = ""
                    after: str = ""
                    end: int = 0
                    for j in range(index - 1, -1, -1):
                        if s[j].isdigit():
                            before = s[j] + before
                            start = j
                        else:
                            break
                    for j in range(index + 1, len(s)):
                        if s[j].isdigit():
                            after = after + s[j]
                            end = j
                        else:
                            break
                    f = s[:start]
                    m = str(int(int(before) / int(after)))
                    e = s[end+1:]
                    s = f + m + e
                    break
                if value == "*":
                    start = 0
                    before: str = ""
                    after: str = ""
                    end = 0
                    for j in range(index - 1, -1, -1):
                        if s[j].isdigit():
                            before = s[j] + before
                            start = j
                        else:
                            break
                    for j in range(index + 1, len(s)):
                        if s[j].isdigit():
                            after = after + s[j]
                            end = j
                        else:
                            break
                    f = s[:start]
                    m = str(int(int(before) * int(after)))
                    e = s[end+1:]
                    s = f + m + e
                    break
        nums = []
        operators = []

        last = None
        if s.startswith("-"):
            nums.append(s[0])
            s = s[1:]
            last = "num"
        for i in s:
            if i.isdigit() and last == "num":
                nums[-1] += i
                last = "num"
            elif i.isdigit() and last != "num":
                nums.append(i)
                last = "num"
            elif i in ("+", "-"):
                operators.append(i)
                last = "op"
        nums = list(map(int, nums))
        result = 0
        if nums:
            result = result + nums[0]
        for i, op in enumerate(operators, 1):
            if op == "-":
                result -= nums[i]
            else:
                result += nums[i]

        return result


solution = Solution()
# print(solution.calculate("1233"))
print(solution.calculate("700+2122-1047+1*2*21*2*2*2*2+1*10*4/4/2*2*3*3*8"))
print(eval("700+2122-1047+1*2*21*2*2*2*2+1*10*4/4/2*2*3*3*8"))

# class Solution:
#     def calculate(self, s: str) -> int:
#         result = 0
#         s = s.replace(" ", "")
#         length = len(s)
#         nums = []
#         high_operators = []
#         low_operators = []
#         operators = []
#         cursor = 0
#         # while cursor <= length:
#         #     cur = s[cursor]
#         #     if cur == "-"
#
#         last = None
#         if s.startswith("-"):
#             nums.append(s[0])
#             s = s[1:]
#             last = "num"
#         for i in s:
#             if i.isdigit() and last == "num":
#                 nums[-1] += i
#                 last = "num"
#             elif i.isdigit() and last != "num":
#                 nums.append(i)
#                 last = "num"
#             elif i in ("*", "/"):
#                 operators.append(i)
#                 last = "op"
#             elif i in ("+", "-"):
#                 operators.append(i)
#                 last = "op"
#         nums = list(map(int, nums))
#         for index, op in enumerate(operators, 1):
#             if op in ("*", "/"):
#                 if op == "*":
#                     num = 0
#             ic(index, op, f"{nums[index -1]} {op} {nums[index]}")
#         ic(nums, operators)
#
#         return int(result)


# def is_leap(x):
#     if (x % 100 == 0) and (x % 400 == 0):
#         return True
#     if (x % 4 == 0) and (x % 100 != 0):
#         return True
#     else:
#         return False
#
#
# is_leap_ = lambda x: True if ((x % 100 == 0) and (x % 400 == 0) or ((x % 4 == 0) and (x %100 != 0)) ) else False

# s = Solution()
# expr = " -43 - 2 * 2  / 2 "
# print(s.calculate(expr))
# print(eval(expr))
