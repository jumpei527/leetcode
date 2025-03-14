import unittest


class Solution:
    def countArrangement(self, arrangement_size: int) -> int:
        """
        Given an integer arrangement_size, return the number of valid
        arrangements where the i-th position meets either of the
        following rules:
        - The number at position i is divisible by i.
        - i is divisible by the number at position i.

        Args:
            arrangement_size (int): The size of the arrangement.

        Returns:
            int: The total number of valid arrangements.
        Example:
            >>> Solution().countArrangement(2)
            2
        """
        self.arr_count = 0
        self.visited = [False] * (arrangement_size + 1)
        FIRST_POSITION = 1
        self.count_with_backtrack(arrangement_size, FIRST_POSITION)
        return self.arr_count

    def count_with_backtrack(self, arr_size: int, position: int) -> None:
        """
        Uses backtracking to count valid arrangements.

        Args:
            arr_size (int): The total size of the arrangement.
            position (int): The current position being filled.

        Example:
            >>> sol = Solution()
            >>> sol.arr_count = 0
            >>> sol.visited = [False] * 3
            >>> sol.count_with_backtrack(2, 1)
            >>> sol.arr_count
            2
        """
        if position > arr_size:
            self.arr_count += 1
            return

        for num in range(1, arr_size+1):
            if not self.visited[num] and self.is_position_valid(num, position):
                self.visited[num] = True
                self.count_with_backtrack(arr_size, position+1)
                self.visited[num] = False

    def is_position_valid(self, num: int, position: int) -> bool:
        """
        Checks if num can be placed at position (1-based index).

        Args:
            num (int): The number to be placed.
            position (int): The current position (1-based index).

        Returns:
            bool: True if the number satisfies the arrangement
            conditions, otherwise False.

        Example:
            >>> sol = Solution()
            >>> sol.is_position_valid(2, 1)
            True
        """
        return num % position == 0 or position % num == 0


class TestCountArrangement(unittest.TestCase):
    def test_countArrangement_large_arrangement(self):
        expected = 41
        result = Solution().countArrangement(7)
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )

    def test_countArrangement_min_arrangement(self):
        expected = 1
        result = Solution().countArrangement(1)
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )
