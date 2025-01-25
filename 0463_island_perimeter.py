# n = len(grid)
# m = len(grid[0])
# Time: O(nm)
# Space: O(1)
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        ISOLATED_ISLAND_PERIMETER = 4

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    perimeter += ISOLATED_ISLAND_PERIMETER - self.countConnectedIslands(grid, row, col)

        return perimeter

    def countConnectedIslands(self, grid: List[List[int]], row: int, col: int) -> int:
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
