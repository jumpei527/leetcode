# n = len(s)
# Time: O(n^2)
# Space: O(1)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        palidrome = s[0]

        for idx in range(len(s)):
            odd = self.expand_from_center(s, idx, idx)
            even = self.expand_from_center(s, idx, idx+1)

            if len(odd) > len(palidrome):
                palidrome = odd
            if len(even) > len(palidrome):
                palidrome = even

        return palidrome

    def expand_from_center(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
