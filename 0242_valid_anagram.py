# Time: O(nlogn)
# Space: O(1)
# n = max(len(s), len(t))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
