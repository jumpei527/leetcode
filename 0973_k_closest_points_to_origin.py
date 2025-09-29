# n = len(points)
# Time: O(n log k)
# Space: O(k)
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap_of_distance = []

        for x, y in points:
            distance = x*x + y*y
            heapq.heappush(max_heap_of_distance, (-distance, (x, y)))
            if len(max_heap_of_distance) > k:
                heapq.heappop(max_heap_of_distance)

        closest_points = []
        for _, point in max_heap_of_distance:
            closest_points.append(point)

        return closest_points
