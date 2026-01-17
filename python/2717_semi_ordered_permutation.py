class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of swaps required to arrange a
        semi-ordered permutation. A semi-ordered permutation is defined
        as one where the first element is 1 and the last element is n.

        Args:
            nums (list[int]): A list of integers representing the permutation.

        Returns:
            int: The minimum number of swaps required to achieve the
            semi-ordered permutation.

        Examples:
            >>> Solution().semiOrderedPermutation([2, 1, 4, 3])
            2
            >>> Solution().semiOrderedPermutation([1, 2, 3, 4])
            0
        """
        num_length = len(nums)

        pos_1 = nums.index(1)
        pos_n = nums.index(num_length)

        swaps_to_front = pos_1
        swaps_to_back = num_length - 1 - pos_n

        overlap = 1 if pos_1 > pos_n else 0

        return swaps_to_front + swaps_to_back - overlap
