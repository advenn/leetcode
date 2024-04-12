from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: Dict[str:List] = {}
        anagram_keys = []
        for str_ in strs:
            sorted_str = sorted(str_)
            sorted_str = "".join(sorted_str)
            print(sorted_str)
            if sorted_str not in anagram_keys:
                anagrams[sorted_str] = [str_]
                anagram_keys.append(sorted_str)
            else:
                anagrams[sorted_str].append(str_)
        return [lst for lst in anagrams.values()]


tc1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(tc1))
