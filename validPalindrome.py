class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s:
            if i.isalpha() or i.isalnum():
                res += i.lower()
        if not res:
            return True
        length = len(res)
        begin = 0
        while begin < length:
            if res[begin] != res[length - 1]:
                return False
            begin += 1
            length -= 1
        return True


