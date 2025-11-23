# n = len(dist)
# m = 10^7
# Time: O(n log m)
# Space: O(1)
import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        train_num = len(dist)
        if train_num - 1 >= hour:
            return -1

        left = 0
        right = 10 ** 7 + 1
        while right - left > 1:
            mid = (left + right) // 2
            if self.can_reach_on_time(dist, hour, mid):
                right = mid
            else:
                left = mid

        return right

    def can_reach_on_time(
        self, dist: List[int], hour: float, speed: int
    ) -> bool:
        total_time = 0
        for idx in range(len(dist)-1):
            total_time += math.ceil(dist[idx] / speed)

        total_time += dist[-1] / speed

        return total_time <= hour
