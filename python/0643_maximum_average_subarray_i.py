# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = 0

        for idx in range(k):
            cur_sum += nums[idx]

        max_sum = cur_sum
        for idx in range(k, len(nums)):
            cur_sum = cur_sum - nums[idx-k] + nums[idx]
            max_sum = max(cur_sum, max_sum)

        return max_sum / k
