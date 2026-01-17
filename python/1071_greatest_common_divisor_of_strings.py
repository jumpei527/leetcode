# n = len(str1)
# m = len(str2)
# Time: O(n + m)
# Space: O(n + m)


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        return str1[:self.gcd(len(str1), len(str2))]

    def gcd(self, source_len: int, target_len: int) -> int:
        while target_len:
            source_len, target_len = target_len, source_len % target_len

        return source_len
