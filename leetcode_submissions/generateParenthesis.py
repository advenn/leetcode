from typing import List


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         if n == 1:
#             return ["()"]
#         else:
#             lst = []
#             for i in range(n):
#                 for j in self.generateParenthesis(i):
#                     for k in self.generateParenthesis(n - 1 - i):
#                         # print(n,i,j,k)
#                         lst.append("(" + j + ")" + k)
#             return lst


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        cases_dct = {1: "(", -1: ")"}
        cases = (1, -1)
        count = 0
        while count < n:
            pr = ""

            for case in cases:
                pr += cases_dct[case]

            lst.append(pr)
            count += 1
        # for i in range(n):
        #     parentheses = ''
        #     latest = 0
        #     if latest == 0:
        #         parentheses += '('
        #         latest = 1
        #     for case in cases:
        #
        #
        #     parentheses += ")"
        #     lst.append(parentheses)
        return lst


s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))
print(s.generateParenthesis(5))
print(s.generateParenthesis(6))
print(s.generateParenthesis(7))
print(s.generateParenthesis(8))
