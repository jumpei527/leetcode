# n = len(matrix)
# m = len(matrix[0])
# Time: O(nm)
# Space: O(nm)
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_num = len(matrix)
        col_num = len(matrix[0])
        x, y = 0, 0
        dx, dy = 1, 0
        spiral_order = []

        for _ in range(row_num * col_num):
            spiral_order.append(matrix[y][x])
            matrix[y][x] = "."

            if (
                not 0 <= x + dx < col_num or
                not 0 <= y + dy < row_num or
                matrix[y + dy][x + dx] == "."
            ):
                dx, dy = -dy, dx

            x += dx
            y += dy

        return spiral_order
