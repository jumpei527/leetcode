# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_positions = {}

        for i, val in enumerate(nums):
            if val in num_positions and i - num_positions[val] <= k:
                return True
            else:
                num_positions[val] = i

        return False
