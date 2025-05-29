# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0
            total += n
            max_sum = max(total, max_sum)

        return max_sum
