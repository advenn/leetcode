class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_lst = list(pattern)
        s_lst = s.split()
        if len(set(pattern_lst)) != len(set(s_lst)) or len(pattern_lst) != len(s_lst):
            return False
        length = len(pattern_lst)
        patterns = {}
        for index in range(length):
            if not patterns.get(pattern_lst[index]):
                patterns[pattern_lst[index]] = s_lst[index]
            else:
                if patterns[pattern_lst[index]] != s_lst[index]:
                    return False

        return True


pattern = "abba"
s = "dog dog dog dog"
solution = Solution()
print(solution.wordPattern(pattern=pattern, s=s))
