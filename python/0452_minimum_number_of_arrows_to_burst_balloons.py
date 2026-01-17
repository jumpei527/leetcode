# n = len(points)
# Time: O(nlogn)
# Space: O(n)
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        points_end = points[0][1]
        arrows = 1

        for point in points[1:]:
            if point[0] > points_end:
                arrows += 1
                points_end = point[1]

        return arrows
