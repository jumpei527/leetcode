# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        prefix_sum = 0

        for idx, num in enumerate(nums):
            if sum_nums - num == prefix_sum * 2:
                return idx
            prefix_sum += num

        return -1
