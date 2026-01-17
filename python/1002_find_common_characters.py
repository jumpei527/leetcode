# n = len(words)
# m is the maximum word length
# Time: O(n * m)
# Space: O(m)
from typing import List
import collections


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        common_char_counts = collections.Counter(words[0])

        for idx in range(1, len(words)):
            char_counts = collections.Counter(words[idx])
            common_char_counts &= char_counts

        result = []
        for char, count in common_char_counts.items():
            result.extend([char] * count)

        return result
