# n = len(target)
# Time: O(n)
# Space: O(1)


class Solution:
    def minFlips(self, target: str) -> int:
        """
        Calculates the minimum suffix flips to match the target string.
        A single flip at index `i` flips all characters from `i` to the end.
        The initial state is assumed to be all '0's.

        Args:
            target (str): The target binary string consisting of '0's and '1's.
        Returns:
            int: The minimum number of flips required.
        Examples:
            >>> Solution().minFlips("101")
            3
            >>> Solution().minFlips("000")
            0
        """
        transitions_count = 0

        # Count transitions between '0' and '1'
        for idx in range(1, len(target)):
            if target[idx-1] != target[idx]:
                transitions_count += 1

        # If the first character is '1', we need an additional flip to start
        initial_flip = 1 if target[0] == "1" else 0

        return transitions_count + initial_flip
