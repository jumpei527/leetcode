# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for idx, num in enumerate(nums):
            if target - num in num_index:
                return [num_index[target - num], idx]

            num_index[num] = idx
