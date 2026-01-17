# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_first_idx = {0: -1}
        prefix_sum = 0

        for idx in range(len(nums)):
            prefix_sum += nums[idx]
            remainder = prefix_sum % k
            if (
                remainder in remainder_first_idx
                and idx - remainder_first_idx[remainder] > 1
            ):
                return True

            if remainder not in remainder_first_idx:
                remainder_first_idx[remainder] = idx

        return False
