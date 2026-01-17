# n = len(intervals)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        merged_intervals = []

        for interval in intervals:
            if newInterval[1] < interval[0]:
                merged_intervals.append(newInterval)
                newInterval = interval
            elif newInterval[0] > interval[1]:
                merged_intervals.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        merged_intervals.append(newInterval)

        return merged_intervals
