# n = len(licensePlate)
# m = len(words)
# Time: O(n + mlogm)
# Space: O(n + m)
from typing import List
from collections import Counter
import unittest


class Solution:
    def shortestCompletingWord(
        self, licensePlate: str, words: List[str]
    ) -> str:
        """
        Receive a string licensePlate and a list of strings words, return the
        shortest completing word in words. A completing word is a word
        that contains all the letters in licensePlate.
        Ignore numbers and spaces in licensePlate, and treat letters as
        case insensitive.
        If a letter appears more than once in licensePlate, then it must
        appear in the word the same number of times or more.
        If there are multiple shortest completing words, return the first
        one that occurs in words.

        Args:
            licensePlate (str): The license plate string.
            words (List[str]): The list of words.

        Returns:
            str: The shortest completing word.

        Examples:
            >>> Solution().shortestCompletingWord(
                    "1s3 PSt", ["step", "steps", "stripe", "stepple"]
                )
            "steps"
        """
        required_chars = []
        for char in licensePlate:
            if char.isalpha():
                required_chars.append(char.lower())
        required_char_counts = Counter(required_chars)

        words.sort(key=len)
        for word in words:
            if self.is_completing_word(word, required_char_counts):
                return word

        return ""

    def is_completing_word(
        self, word: str, required_char_counts: Counter
    ) -> bool:
        """
        Check if the given word contains all the required characters in the
        required_char_counts Counter.

        Args:
            word (str): The word to check.
            required_char_counts (Counter): The required characters.

        Returns:
            bool: True if the word contains all the required characters.

        Examples:
            >>> Solution().is_completing_word(
                    "steps", Counter({'s': 2, 'p': 1, 't': 1})
                )
            True
            >>> Solution().is_completing_word(
                    "stepple", Counter({'s': 2, 'p': 1, 't': 1})
                )
            False
        """
        return Counter(word) >= required_char_counts


class TestShortestCompletingWord(unittest.TestCase):
    def test_example_1(self):
        licensePlate = "1s3 PSt"
        words = ["step", "steps", "stripe", "stepple"]
        expected = "steps"
        result = Solution().shortestCompletingWord(licensePlate, words)
        self.assertEqual(result, expected)

    def test_example_2(self):
        licensePlate = "1s3 456"
        words = ["looks", "pest", "stew", "show"]
        expected = "pest"
        result = Solution().shortestCompletingWord(licensePlate, words)
        self.assertEqual(result, expected)
