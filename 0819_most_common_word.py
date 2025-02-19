# n = len(paragraph)
# Time: O(n)
# Space: O(n)
from typing import List
from collections import Counter
import unittest


class Solution:
    def mostCommonWord(
        self, paragraph: str, banned: List[str]
    ) -> str:
        """
        Receives a paragraph and a list of banned words.
        Returns the most common word that is not in the list of banned words.

        Args:
            paragraph (str): The paragraph to analyze.
            banned (List[str]): The list of banned words.

        Returns:
            str: The most common word that is not in the list of banned words.

        Examples:
            >>> Solution().mostCommonWord(
                    "Bob hit a ball, the hit BALL flew far after it was hit.",
                    ["hit"]
                )
            'ball'
        """
        split_symbols = "!?',;."
        for char in split_symbols:
            paragraph = paragraph.replace(char, " ")
        words_counts = Counter(paragraph.lower().split())

        return self.findMostFrequentWord(words_counts, banned)

    def findMostFrequentWord(
        self, words_counts: Counter, banned: List[str]
    ) -> str:
        """
        Receives a Counter of words and a list of banned words.
        Returns the most common word that is not in the list of banned words.

        Args:
            words_counts (Counter): The Counter of words.
            banned (List[str]): The list of banned words.

        Returns:
            str: The most common word that is not in the list of banned words.

        Examples:
            >>> words_counts = Counter({
                    "bob": 1, "hit": 3, "a": 1, "ball": 2, "the": 1,
                    "flew": 1, "far": 1, "after": 1, "it": 1, "was": 1
                })
            >>> Solution().find_common_word(words_counts, ["hit"])
            'ball'
        """
        common_word = ""
        max_count = 0
        for word, count in words_counts.items():
            if word not in banned and count > max_count:
                common_word = word
                max_count = count

        return common_word


class TestMostCommonWord(unittest.TestCase):
    def test_most_frequent_word_excluding_banned(self):
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        expected = "ball"
        result = Solution().mostCommonWord(paragraph, banned)
        self.assertEqual(
            result, expected, f"Expected {expected}, but got {result}"
        )

    def test_single_word_paragraph(self):
        paragraph = "a."
        banned = []
        expected = "a"
        result = Solution().mostCommonWord(paragraph, banned)
        self.assertEqual(
            result, expected, f"Expected {expected}, but got {result}"
        )

    def test_all_words_banned(self):
        paragraph = "apple apple banana"
        banned = ["apple", "banana"]
        expected = ""
        result = Solution().mostCommonWord(paragraph, banned)
        self.assertEqual(
            result, expected, f"Expected {expected}, but got {result}"
        )
