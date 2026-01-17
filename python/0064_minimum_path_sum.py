# n = len(grid)
# m = len(grid[0])
# Time: O(n * m)
# Space: O(1)
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i > 0 and j > 0:
                    min_path = min(grid[i-1][j], grid[i][j-1])
                elif j > 0:
                    min_path = grid[i][j-1]
                elif i > 0:
                    min_path = grid[i-1][j]
                else:
                    min_path = 0
                grid[i][j] += min_path

        return grid[-1][-1]
