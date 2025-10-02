# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_freq = {0: 1}
        prefix_sum = 0
        total_subarray = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_sum_freq:
                total_subarray += prefix_sum_freq[prefix_sum - k]

            prefix_sum_freq[prefix_sum] = (
                prefix_sum_freq.get(prefix_sum, 0) + 1
            )

        return total_subarray
