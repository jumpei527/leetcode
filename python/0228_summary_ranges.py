# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        summary_ranges = []
        start = nums[0]

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] - nums[i-1] != 1:
                if start == nums[i-1]:
                    summary_ranges.append(str(start))
                else:
                    summary_ranges.append(f"{start}->{nums[i-1]}")
                if i != len(nums):
                    start = nums[i]

        return summary_ranges
