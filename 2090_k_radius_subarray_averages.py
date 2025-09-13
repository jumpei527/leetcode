# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        nums_length = len(nums)
        window_size = 2 * k + 1
        avgs = [-1] * nums_length
        if window_size > nums_length:
            return avgs

        k_radius_sum = 0
        for idx in range(window_size):
            k_radius_sum += nums[idx]

        avgs[k] = k_radius_sum // window_size
        for idx in range(k+1, nums_length - k):
            k_radius_sum = k_radius_sum - nums[idx - k - 1] + nums[idx + k]
            avgs[idx] = k_radius_sum // window_size

        return avgs
