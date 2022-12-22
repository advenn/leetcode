"""
leetcode link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters_on_nums = {
            '2': set('abc'),
            '3': set("def"),
            '4': set('ghi'),
            '5': set('jkl'),
            '6': set('mno'),
            '7': set('pqrs'),
            '8': set('tuv'),
            '9': set('wxyz')
        }
        if len(digits) == 1:
            return list(letters_on_nums[digits])
        base_letters = letters_on_nums[digits[0]]
        length = len(digits)
        result = list(base_letters)
        for i in range(1, length):
            numset = letters_on_nums[digits[i]]
            oraliq = result.copy()
            result = []
            for ora in oraliq:
                for adding in numset:
                    result.append(ora+adding)
        return result


res4_234 = ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg",
            "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]
s = Solution()
print(sorted(res4_234) == sorted(s.letterCombinations('234')))

#         return result
#
s = Solution()
print(s.letterCombinations('2344'))
