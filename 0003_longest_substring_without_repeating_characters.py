# n = len(s)
class Solution:
    # Time: O(n^3)
    # Space: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_len = 0
        for i in range(len(s)):
            unique_chars = []
            j = i
            tmp = 0
            while j < len(s) and s[j] not in unique_chars:
                unique_chars.append(s[j])
                tmp += 1
                j += 1
            substr_len = max(substr_len, tmp)
        return substr_len

    # Time: O(n)
    # Space: O(n)
    def lengthOfLongestSubstring2(self, s: str) -> int:
        unique_chars = {}
        max_len = 0
        start = 0
        for end in range(len(s)):
            if s[end] not in unique_chars:
                max_len = max(max_len, end - start + 1)
            else:
                if unique_chars[s[end]] < start:
                    max_len = max(max_len, end - start + 1)
                else:
                    start = unique_chars[s[end]] + 1
            unique_chars[s[end]] = end
        return max_len
