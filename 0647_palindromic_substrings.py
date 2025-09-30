# n = len(s)
# Time: O(n^2)
# Space: O(1)


class Solution:
    def countSubstrings(self, s: str) -> int:
        self.total_count = 0

        for idx in range(len(s)):
            self.expand_pelindrome(s, idx, idx)
            self.expand_pelindrome(s, idx, idx+1)

        return self.total_count

    def expand_pelindrome(self, s: str, left: int, right: int) -> None:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.total_count += 1
            left -= 1
            right += 1

        return
