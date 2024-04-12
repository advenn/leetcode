from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        users = dict(zip(names, heights))
        users = {
            k: v for k, v in (sorted(users.items(), key=lambda x: x[1], reverse=True))
        }
        return list(users.keys())


s = Solution()
print(s.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
