# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        nums_length = len(nums)
        if nums_length < 3:
            return 0

        max_on_left = [0] * nums_length
        max_on_right = [0] * nums_length

        left_max = 0
        for i in range(nums_length):
            max_on_left[i] = left_max
            left_max = max(nums[i], left_max)

        right_max = 0
        for i in range(nums_length - 1, -1, -1):
            max_on_right[i] = right_max
            right_max = max(nums[i], right_max)

        max_value = 0
        for i in range(1, nums_length - 1):
            cur_value = (max_on_left[i] - nums[i]) * max_on_right[i]
            max_value = max(cur_value, max_value)

        return max_value
