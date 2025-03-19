# n = len(original_str)
# Time: O(nlogn)
# Space: O(n)
import unittest
from returns.result import Result, Failure, Success


class Solution:
    def reorganizeString(
            self, original_str: str
    ) -> Result[str, Exception]:
        """
        Given a string original_str, check if the letters can be
        rearranged so that two characters that are adjacent to each
        other are not the same.
        If possible, return any valid arrangement. If not possible,
        return the empty string.

        Args:
            original_str: a string of lowercase letters

        Returns:
            Result[str, Exception]: A success result with a rearranged
            string (which may be empty if rearrangement is impossible),
            or a failure result with an error message.

        Examples:
            >>> Solution().reorganizeString('aab')
            Success('aba')
            >>> Solution().reorganizeString('aaab')
            Success('')
        """
        if not original_str:
            return Failure("The string is empty")

        freq_map = {}
        for char in original_str:
            freq_map[char] = freq_map.get(char, 0) + 1

        sorted_freq_map = sorted(
            freq_map.items(), key=lambda x: x[1], reverse=True
        )

        most_char_freq = sorted_freq_map[0][1]
        if most_char_freq > (len(original_str) + 1) // 2:
            return Success("")

        return Success(self.arrange_chars_alternately(
            sorted_freq_map, len(original_str)
        ))

    def arrange_chars_alternately(
            self, sorted_freq_map: list[tuple[str, int]], length: int
    ) -> str:
        """
        Construct and return a valid rearrangement of characters such
        that no two adjacent characters are the same.
        The function places characters in alternating positions
        (even indices first, then odd indices) to ensure that
        high-frequency characters are spaced apart.

        Args:
            sorted_freq_map (list[tuple[str, int]]): A list of
                (character, frequency) tuples, sorted in descending
                order by frequency.
            length (int): The length of the original string.

        Returns:
            str: a string that satisfies the condition

        Examples:
            >>> Solution().arrange_chars_alternately(
            [('a', 2), ('b', 1)], 3
            )
            'aba'
        """
        reorganized_arr = [None] * length
        idx = 0
        for char, freq in sorted_freq_map:
            for _ in range(freq):
                reorganized_arr[idx] = char
                idx += 2
                if idx >= length:
                    idx = 1

        return "".join(reorganized_arr)


class TestReorganizeString(unittest.TestCase):
    def test_reorganizeString_possible_rearrangement(self):
        expected = Success("aba")
        result = Solution().reorganizeString("aab")
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )

    def test_reorganizeString_impossible_rearrangement(self):
        expected = Success("")
        result = Solution().reorganizeString("aaab")
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )

    def test_reorganizeString_single_char(self):
        expected = Success("a")
        result = Solution().reorganizeString("a")
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )

    def test_reorganizeString_two_chars(self):
        expected = Failure(Exception("The string is empty"))
        result = Solution().reorganizeString("")
        self.assertEqual(str(result.failure()), str(expected.failure()))
