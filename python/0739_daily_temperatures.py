# n = len(temperatures)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait_days = [0] * len(temperatures)
        pending_days = []

        for cur_day in range(len(temperatures)):
            while (
                pending_days and
                temperatures[cur_day] > temperatures[pending_days[-1]]
            ):
                prev_day = pending_days.pop()
                wait_days[prev_day] = cur_day - prev_day
            pending_days.append(cur_day)

        return wait_days
