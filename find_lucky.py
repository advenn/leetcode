from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        cnt = Counter(arr)
        srt = sorted(cnt)
        luckiest = -1
        for k, v in cnt.items():
            if k == v and k >= luckiest:
                luckiest = k
        return luckiest


s = Solution()

print(s.findLucky([1, 2, 2, 3, 3, 3]),
      s.findLucky([2, 2, 2, 3, 3]),
      s.findLucky([2, 2, 3, 4]))
