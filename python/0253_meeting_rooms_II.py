# n = len(intervals)
# Time: O(nlogn)
# Space: O(n)
from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        required_room = []

        heapq.heappush(required_room, intervals[0][1])
        for start, end in intervals[1:]:
            if start >= required_room[0]:
                heapq.heappop(required_room)
            heapq.heappush(required_room, end)

        return len(required_room)
