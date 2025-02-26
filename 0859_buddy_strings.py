# n = len(s)
# Time: O(n)
# Space: O(n)
import unittest


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        """
        Given two strings s and goal, return true if you can swap two
        letters in s so the result is equal to goal, otherwise, return
        false.

        Args:
            s (str): A string of lowercase English letters.
            goal (str): A string of lowercase English letters.

        Returns:
            bool: True if you can swap two letters in s so the result is
            equal to goal, otherwise, return false.

        Example:
            >>> Solution().buddyStrings('ab', 'ba')
            True
        """
        s_length = len(s)
        goal_length = len(goal)
        if s_length != goal_length:
            return False

        diff_idx = []

        for idx in range(s_length):
            if s[idx] != goal[idx]:
                diff_idx.append(idx)

        if len(diff_idx) == 2:
            return self.is_equal_after_swap(s, goal, diff_idx)

        if not diff_idx and s_length != len(set(s)):
            return True

        return False

    def is_equal_after_swap(self, s: str, goal: str, diff_idx: list) -> bool:
        """
        Given two strings s and goal and a list of two indexes that are
        different in the two strings, return true if the two strings are
        equal after swapping the two characters at the given indexes,
        otherwise, return false.

        Args:
            s (str): A string of lowercase English letters.
            goal (str): A string of lowercase English letters.
            diff_idx (list): A list of two indexes that are different
            in the two strings.

        Returns:
            bool: True if the two strings are equal after swapping the
            two characters at the given indexes, otherwise, return false.

        Example:
            >>> Solution().is_equal_after_swap('ab', 'ba', [0, 1])
            True
            >>> Solution().is_equal_after_swap('ab', 'ab', [0, 1])
            False
        """
        i, j = diff_idx
        return s[i] == goal[j] and s[j] == goal[i]


class TestBuddyStrings(unittest.TestCase):
    def test_swap_two_different_chars(self):
        s = 'ab'
        goal = 'ba'
        expected = True
        result = Solution().buddyStrings(s, goal)
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )

    def test_no_swap_strings(self):
        s = 'ab'
        goal = 'ab'
        expected = False
        result = Solution().buddyStrings(s, goal)
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )

    def test_no_swap_strings_with_duplicate_chars(self):
        s = 'aa'
        goal = 'aa'
        expected = True
        result = Solution().buddyStrings(s, goal)
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )
