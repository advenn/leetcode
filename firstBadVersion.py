# The isBadVersion API is already defined for you.
import random

a = random.randint(1, 1000)
b = random.randint(1, 1000)
n = a + b
print(a, b, n)
versions = [False for _ in range(a)] + [True for _ in range(b)]
print(versions[a-1])




def isBadVersion(version: int) -> bool:
    return versions[version]


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Input: n = 5, bad = 4
        Output: 4
        Explanation:
        call isBadVersion(3) -> false
        call isBadVersion(5) -> true
        call isBadVersion(4) -> true
        Then 4 is the first bad version.
        true -> false
        """
        # """[True, True, True, True, False, False]"""
        low = 0
        high = n
        mid = 0
        while True:
            mid = (high + low) // 2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif not isBadVersion(mid) and isBadVersion(mid+1):
                return mid + 1
            elif not isBadVersion(mid):
                low = mid
            else:
                high = mid

        # def binary_search(arr, x):
        #     low = 0
        #     high = len(arr) - 1
        #     mid = 0
        #     while low <= high:
        #         mid = (high + low) // 2
        #         if arr[mid] < x:
        #             low = mid + 1
        #         elif arr[mid] > x:
        #             high = mid - 1
        #         else:
        #             return mid
        #     return -1
        # binary_search(n)


s = Solution()
print(s.firstBadVersion(n))
