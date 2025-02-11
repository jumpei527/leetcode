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
        alpha_chars = []
        for char in licensePlate:
            if char.isalpha():
                alpha_chars.append(char.lower())
        alpha_count = Counter(alpha_chars)

        words.sort(key=len)
        for word in words:
            if Counter(word) >= alpha_count:
                return word

        return ""


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
