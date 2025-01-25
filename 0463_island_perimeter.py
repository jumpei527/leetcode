# n = len(grid)
# m = len(grid[0])
# Time: O(nm)
# Space: O(1)
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        perimeter = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    perimeter += 4 - self.countConnectedIslands(grid, r, c)

        return perimeter

    def countConnectedIslands(self, grid: List[List[int]], row, col):
        count = 0

        if row > 0 and grid[row-1][col] == 1:
            count += 1
        if row < len(grid) - 1 and grid[row+1][col] == 1:
            count += 1
        if col > 0 and grid[row][col-1] == 1:
            count += 1
        if col < len(grid[0]) - 1 and grid[row][col+1] == 1:
            count += 1

        return count
