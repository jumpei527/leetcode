# n = len(words)
# m = len(chars)
# Time: O(n * m)
# Space: O(m)
from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_length = 0
        source_char_freq = Counter(chars)

        for word in words:
            target_char_freq = Counter(word)
            can_form_word = True
            for c in target_char_freq:
                if target_char_freq[c] > source_char_freq[c]:
                    can_form_word = False
                    break

            if can_form_word:
                total_length += len(word)

        return total_length
