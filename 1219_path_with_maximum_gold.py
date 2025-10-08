# n = len(grid)
# m = len(grid[0])
# Time: O(n * m * 3^(n*m))
# Space: O(n * m)
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = 0
        self.row_size = len(grid)
        self.col_size = len(grid[0])

        for i in range(self.row_size):
            for j in range(self.col_size):
                if grid[i][j] != 0:
                    gold = self.calculate_sum_gold(i, j, grid)
                    max_gold = max(gold, max_gold)

        return max_gold

    def calculate_sum_gold(
        self, i: int, j: int, grid: List[List[int]]
    ) -> int:
        original_gold = grid[i][j]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        grid[i][j] = 0
        max_from_neighbors = 0
        for dr, dc in directions:
            row = i + dr
            col = j + dc
            if self.isBound(row, col) and grid[row][col] != 0:
                cur_gold = self.calculate_sum_gold(row, col, grid)
                max_from_neighbors = max(cur_gold, max_from_neighbors)

        grid[i][j] = original_gold

        return original_gold + max_from_neighbors

    def isBound(self, row: int, col: int) -> bool:
        return 0 <= row < self.row_size and 0 <= col < self.col_size
