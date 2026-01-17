# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        count = 0
        left = 0
        right = 0
        nums_length = len(nums)

        while right < nums_length:
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += 1 + (right - left)
            right += 1

        return count
