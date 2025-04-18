# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_num = 0
        left = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    k += 1
                left += 1

            max_num = max(right - left + 1, max_num)

        return max_num
