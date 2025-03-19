# n = len(tasks)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        idle_map = {}
        total_days = 0
        for task in tasks:
            if task in idle_map and total_days <= idle_map[task]:
                total_days = idle_map[task]
            total_days += 1
            idle_map[task] = total_days + space

        return total_days
