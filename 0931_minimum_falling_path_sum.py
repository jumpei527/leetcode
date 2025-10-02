# n = len(matrix)
# Time: O(n^2)
# Space: O(1)
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        grid_size = len(matrix)

        for i in range(1, grid_size):
            for j in range(grid_size):
                path_min = matrix[i-1][j] + matrix[i][j]
                if j-1 >= 0:
                    path_min = min(matrix[i-1][j-1] + matrix[i][j], path_min)
                if j+1 < grid_size:
                    path_min = min(matrix[i-1][j+1] + matrix[i][j], path_min)

                matrix[i][j] = path_min

        return min(matrix[-1])
