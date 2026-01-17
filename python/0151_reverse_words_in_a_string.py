# n = len(s)
# Time: O(n)
# Space: O(n)


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s_reversed = s[::-1]
        return " ".join(s_reversed)
