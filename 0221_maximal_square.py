# n, m = len(matrix), len(matrix[0])
# Time: O(nm)
# Space: O(nm)
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        side_length = [[0] * (cols+1) for _ in range(rows+1)]
        max_size = 0

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if matrix[r-1][c-1] == "1":
                    side_length[r][c] = min(
                        side_length[r-1][c-1],
                        side_length[r-1][c],
                        side_length[r][c-1]
                    ) + 1
                    max_size = max(max_size, side_length[r][c])

        return max_size * max_size
