# n = len(board) * len(board[0])
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_length = len(board)
        col_length = len(board[0])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]

        for i in range(row_length):
            for j in range(col_length):
                count = 0
                for dr, dc in directions:
                    row = i + dr
                    col = j + dc
                    if (0 <= row < row_length and
                            0 <= col < col_length and
                            abs(board[row][col]) == 1):
                        count += 1

                if (count < 2 or 3 < count) and board[i][j] == 1:
                    board[i][j] = -1
                if count == 3 and board[i][j] == 0:
                    board[i][j] = 2

        for i in range(row_length):
            for j in range(col_length):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == -1:
                    board[i][j] = 0

        return board
