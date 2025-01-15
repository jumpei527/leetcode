# n = len(triangle)
# Time: O(n^2)
# Space: O(1)
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                min_sum = min(triangle[i+1][j], triangle[i+1][j+1])
                triangle[i][j] += min_sum

        return triangle[0][0]
