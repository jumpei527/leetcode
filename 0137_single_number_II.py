# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List
import unittest
from returns.result import Result, Failure, Success


class Solution:
    def singleNumber(self, nums: List[int]) -> Result[str, Exception]:
        """
        Given a list of integers where each integer appears three times
        except for one integer which appears once, find that single
        integer.

        Args:
            nums: A list of integers where each integer appears three
            times except for one integer which appears once.
        Returns:
            int: The integer that appears only once in the list.
        Examples:
            >>> Solution().singleNumber([2, 2, 3, 2])
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
                bit_sum += (num >> bit_idx) & BIT_MASK
            bit_sum %= REPEAT_COUNT
            single_num |= bit_sum << bit_idx

        return single_num


class TestSingleNumber(unittest.TestCase):
    def test_singleNumber_negative_number(self):
        expected = Success(-1)
        result = Solution().singleNumber([-2, -2, -1, -2])
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )

    def test_singleNumber_empty_list(self):
        expected = Failure("The list is empty.")
        result = Solution().singleNumber([])
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )
