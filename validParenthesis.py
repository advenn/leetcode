class Solution:
    def isValid(self, s: str) -> bool:
        """
        ()[]{}
        ()([]{})
        ()([]{})()
        {}}{
        """
        cache = []
        for p in s:
            if p in ("(", "[", "{"):
                cache.append(p)
            elif p == ")" and cache and cache[-1] == "(":
                cache.pop()
            elif p == "]" and cache and cache[-1] == "[":
                cache.pop()
            elif p == "}" and cache and cache[-1] == "{":
                cache.pop()
            else:
                return False
        return len(cache) == 0


"()[]{}"
"()([]{})"
s = Solution()
print(s.isValid("()([]{})()"))
print(s.isValid("{}}{"))
print(s.isValid("(])"))



