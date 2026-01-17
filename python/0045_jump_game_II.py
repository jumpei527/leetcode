# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = 0
        cur_reach = 0
        next_reach = 0

        for idx in range(len(nums) - 1):
            next_reach = max(next_reach, idx + nums[idx])
            if idx == cur_reach:
                jump_count += 1
                cur_reach = next_reach

        return jump_count
