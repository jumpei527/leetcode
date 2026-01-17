# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        length = len(nums)
        after_length = length
        front_idx = 0
        back_idx = (length + 1) // 2

        while front_idx < (length + 1) // 2 and back_idx < length:
            if nums[front_idx] < nums[back_idx]:
                after_length -= 2
            front_idx += 1
            back_idx += 1

        return after_length
