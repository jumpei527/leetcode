# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] <= nums[right]:
            return nums[left]

        while (right - left) > 1:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        return nums[right]
