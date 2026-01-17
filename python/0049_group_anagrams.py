# n = len(strs)
# m = max(len(s) for s in strs)
# Time: O(nmlogm)
# Space: O(nm)
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            anagram_map[key].append(s)

        return list(anagram_map.values())
