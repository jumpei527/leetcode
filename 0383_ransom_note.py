# n = len(ransomNote)
# m = len(magazine)
# Time: O(n+m)
# Space: O(1)


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = {}

        for c in magazine:
            hash[c] = 1 + hash.get(c, 0)

        for c in ransomNote:
            if c not in magazine or hash[c] <= 0:
                return False
            hash[c] -= 1

        return True
