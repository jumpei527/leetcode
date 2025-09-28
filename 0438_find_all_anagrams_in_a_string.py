# n = len(s)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_freq = {}
        target_freq = {}
        target_len = len(p)
        source_len = len(s)
        anagram_idx = []

        if target_len > source_len:
            return anagram_idx

        for char in p:
            target_freq[char] = target_freq.get(char, 0) + 1

        for idx in range(len(p)):
            char = s[idx]
            window_freq[char] = window_freq.get(char, 0) + 1

        if window_freq == target_freq:
            anagram_idx.append(0)

        for idx in range(len(s) - target_len):
            window_freq[s[idx]] -= 1
            if window_freq[s[idx]] == 0:
                del window_freq[s[idx]]
            window_freq[s[idx + target_len]] = (
                window_freq.get(s[idx + target_len], 0) + 1
            )
            if window_freq == target_freq:
                anagram_idx.append(idx+1)

        return anagram_idx
