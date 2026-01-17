# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        idx = 0

        while idx <= right:
            if nums[idx] == 0:
                nums[left], nums[idx] = nums[idx], nums[left]
                left += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx], nums[right] = nums[right], nums[idx]
                right -= 1
            else:
                idx += 1
