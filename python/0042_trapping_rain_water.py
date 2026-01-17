# n = len(height)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_wall = [0] * len(height)
        right_wall = [0] * len(height)

        cur_high = 0
        for idx in range(len(height)):
            cur_high = max(height[idx], cur_high)
            left_wall[idx] = cur_high

        cur_high = 0
        for idx in range(len(height)-1, -1, -1):
            cur_high = max(height[idx], cur_high)
            right_wall[idx] = cur_high

        total_water = 0
        for idx in range(len(height)):
            wall_height = min(left_wall[idx], right_wall[idx])
            total_water += wall_height - height[idx]

        return total_water
