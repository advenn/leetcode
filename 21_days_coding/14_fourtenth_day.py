from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s = ['_' for i in range(len(s))]
        lets = {index: real for index, real in enumerate(indices)}  # dict(zip(list(range(len(s))), indices))
        for k, v in lets.items():
            new_s[v] = s[k]
        return ''.join(new_s)


s = Solution()
print(s.restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))
