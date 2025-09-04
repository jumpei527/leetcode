# n = len(nums)
# Time: O(nlogn)
# Space: O(n)
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        smaller_counts_map = {}
        for idx, num in enumerate(sorted_nums):
            if num not in smaller_counts_map:
                smaller_counts_map[num] = idx

        return [smaller_counts_map[num] for num in nums]
