# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List
import unittest
from returns.result import Result, Failure, Success


class Solution:
    def find_single_number(self, nums: List[int]) -> Result[int, str]:
        """
        Given a list of integers where each integer appears three times
        except for one integer which appears once, find that single
        integer.

        Args:
            nums: A list of integers where each integer appears three
            times except for one integer which appears once.
        Returns:
            Result[int, str]: A success result with the single
            integer, or a failure result with an error message.
        Examples:
            >>> Solution().find_single_number([2, 2, 3, 2])
            Success(3)
        """
        if not nums:
            return Failure("The list is empty.")

        INT_MAX = 2**31
        UINT_MAX = 2**32

        single_num = self.build_single_number_from_bits(nums)

        # If the number is negative, we need to convert it to a signed integer
        if single_num >= INT_MAX:
            single_num -= UINT_MAX

        return Success(single_num)

    def build_single_number_from_bits(self, nums: List[int]) -> int:
        """
        Build the single number from the bits of the numbers in the list.

        Args:
            nums: A list of integers where each integer appears three
            times except for one integer which appears once.
        Returns:
            int: The integer that appears only once in the list.
        Examples:
            >>> Solution().build_single_number_from_bits([2, 2, 3, 2])
            3
        """
        BIT_LENGTH = 32
        REPEAT_COUNT = 3
        BIT_MASK = 1

        single_num = 0

        for bit_idx in range(BIT_LENGTH):
            bit_sum = 0
            for num in nums:
                # Count how many times 1 appears at this bit position
                bit_sum += (num >> bit_idx) & BIT_MASK
            # Eliminate the effect of numbers that appear three times
            bit_sum %= REPEAT_COUNT
            # Set the bit in the final result
            single_num |= bit_sum << bit_idx

        return single_num


class TestSolution(unittest.TestCase):
    def test_find_single_number_positive_number(self):
        expected = Success(3)
        result = Solution().find_single_number([2, 2, 3, 2])
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}."
        )

    def test_find_single_number_negative_number(self):
        expected = Success(-1)
        result = Solution().find_single_number([-2, -2, -1, -2])
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}."
        )

    def test_find_single_number_empty_list(self):
        expected = Failure("The list is empty.")
        result = Solution().find_single_number([])
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}."
        )
