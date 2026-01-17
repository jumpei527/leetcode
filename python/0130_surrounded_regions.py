# n = len(board)
# m = len(board[0])
# Time: O(nm)
# Space: O(nm)
from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        col_length = len(board)
        row_length = len(board[0])
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row_idx in range(row_length):
            if board[0][row_idx] == "O":
                queue.append((0, row_idx))
            if board[col_length - 1][row_idx] == "O":
                queue.append((col_length - 1, row_idx))

        for col_idx in range(col_length):
            if board[col_idx][0] == "O":
                queue.append((col_idx, 0))
            if board[col_idx][row_length - 1] == "O":
                queue.append((col_idx, row_length - 1))

        while queue:
            i, j = queue.popleft()
            board[i][j] = "#"

            for di, dj in directions:
                c, r = i + di, j + dj
                if (
                    0 <= c < col_length and
                    0 <= r < row_length and
                    board[c][r] == "O"
                ):
                    board[c][r] = "#"
                    queue.append((c, r))

        for col_idx in range(col_length):
            for row_idx in range(row_length):
                if board[col_idx][row_idx] == "O":
                    board[col_idx][row_idx] = "X"
                if board[col_idx][row_idx] == "#":
                    board[col_idx][row_idx] = "O"
