# n = len(tasks)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = {}
        for task in tasks:
            freq_map[task] = freq_map.get(task, 0) + 1

        sorted_freq_map = sorted(
            freq_map.items(), key=lambda x: x[1], reverse=True
        )

        idle_group = sorted_freq_map[0][1] - 1
        idle = idle_group * n
        for _, freq in sorted_freq_map[1:]:
            idle -= min(idle_group, freq)

        return len(tasks) + idle if idle >= 0 else len(tasks)
