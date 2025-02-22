# n = len(intervals)
# Time: O(nlogn)
# Space: O(n)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []

        prev = intervals[0]

        for interval in intervals:
            if interval[0] <= prev[1]:
                prev[1] = max(interval[1], prev[1])
            else:
                merged_intervals.append(prev)
                prev = interval

        merged_intervals.append(prev)
        return merged_intervals
