# n = len(s)
# Time: O(n)
# Space: O(n)
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = defaultdict(int)

        for char in s:
            count_map[char] = count_map.get(char, 0) + 1

        for idx, char in enumerate(s):
            if count_map[char] == 1:
                return idx

        return -1
