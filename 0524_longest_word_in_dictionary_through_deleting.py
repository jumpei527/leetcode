# n = len(dictionary)
from typing import List


class Solution:
    # Time: O(nlogn)
    # Space: O(1)
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        sorted_dictionary = sorted(dictionary, key=lambda x: (-len(x), x))

        for word in sorted_dictionary:
            if self.is_subsequence(word, s):
                return word

        return ""

    def is_subsequence(self, sub: str, text: str) -> bool:
        sub_idx = 0
        text_idx = 0

        while sub_idx < len(sub) and text_idx < len(text):
            if sub[sub_idx] == text[text_idx]:
                sub_idx += 1
            text_idx += 1

        return sub_idx == len(sub)


class Solution2:
    # Time: O(n)
    # Space: O(1)
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longest_word = ""

        for word in dictionary:
            if self.is_subsequence(word, s):
                if len(word) > len(longest_word):
                    longest_word = word
                if len(word) == len(longest_word) and word < longest_word:
                    longest_word = word

        return longest_word

    def is_subsequence(self, sub: str, text: str) -> bool:
        sub_idx = 0
        text_idx = 0

        while sub_idx < len(sub) and text_idx < len(text):
            if sub[sub_idx] == text[text_idx]:
                sub_idx += 1
            text_idx += 1

        return sub_idx == len(sub)
