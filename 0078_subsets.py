# n = len(nums)
# Time: O(2^n)
# Space: O(2^n)
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets of a list of integers.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[List[int]]: A list of all possible subsets.

        Example:
            Input: nums = [1, 2, 3]
            Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        """
        subsets_result = []

        def generate_subsets(
            start_idx: int = 0, cur_subset: List[int] = []
        ) -> None:
            """
            Helper function to generate subsets using backtracking.

            Args:
                start_idx (int): The starting index for generating subsets.
                cur_subset (List[int]): The current subset being built.

            Returns:
                None: This function modifies subsets_result in place.
            """
            subsets_result.append(cur_subset[:])
            for idx in range(start_idx, len(nums)):
                cur_subset.append(nums[idx])
                generate_subsets(idx + 1, cur_subset)
                cur_subset.pop()

        generate_subsets()
        return subsets_result
