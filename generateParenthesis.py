from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            lst = []
            for i in range(n):
                for j in self.generateParenthesis(i):
                    for k in self.generateParenthesis(n - 1 - i):
                        print(n,i,j,k)
                        lst.append("(" + j + ")" + k)
            return lst

s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))
print(s.generateParenthesis(5))
print(s.generateParenthesis(6))
print(s.generateParenthesis(7))
print(s.generateParenthesis(8))
print(s.generateParenthesis(9))
print(s.generateParenthesis(10))