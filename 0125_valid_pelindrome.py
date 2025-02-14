# n = len(s)
# Time: O(n)
# Space: O(n)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_formatted = []
        for i in range(len(s)):
            if s[i].isalnum():
                s_formatted.append(s[i].lower())
        if s_formatted == s_formatted[::-1]:
            return True
        return False
