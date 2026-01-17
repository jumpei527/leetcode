# n = len(intervals)
# Time: O(n log n)
# Space: O(n)
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_with_idx = [
            (start, idx) for idx, (start, _) in enumerate(intervals)
        ]
        start_with_idx.sort()

        def find_right_interval_idx(end_idx):
            left = -1
            right = len(intervals)
            while right - left > 1:
                mid = (left + right) // 2
                if start_with_idx[mid][0] >= end:
                    right = mid
                else:
                    left = mid
            return start_with_idx[right][1] if right != len(intervals) else -1

        results = []
        for _, end in intervals:
            right_interval_idx = find_right_interval_idx(end)
            results.append(right_interval_idx)
        return results
