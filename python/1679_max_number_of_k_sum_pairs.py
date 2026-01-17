# n = len(nums)
# Time: O(nlogn)
# Space: O(1)
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left_idx = 0
        right_idx = len(nums) - 1
        count = 0

        while left_idx < right_idx:
            if nums[left_idx] + nums[right_idx] == k:
                left_idx += 1
                right_idx -= 1
                count += 1
            elif nums[left_idx] + nums[right_idx] > k:
                right_idx -= 1
            else:
                left_idx += 1

        return count
