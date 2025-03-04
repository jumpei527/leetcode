# n = len(nums)
# Time: O(logn)
# Space: O(1)
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.search_left_idx(nums, target)
        right = self.search_right_idx(nums, target)

        if 0 <= left < len(nums) and nums[left] == target:
            return [left, right]
        return [-1, -1]

    def search_left_idx(self, nums: List[int], target: int) -> List[int]:
        left = -1
        right = len(nums)

        while (right - left) > 1:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        return right

    def search_right_idx(self, nums: List[int], target: int) -> List[int]:
        left = -1
        right = len(nums)

        while (right - left) > 1:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        return left
