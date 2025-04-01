# Time: O(1)
# Space: O(1)
from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        ROW_NUM = 9
        COL_NUM = 9
        for row in range(ROW_NUM):
            for col in range(COL_NUM):
                if board[row][col] == ".":
                    continue

                box_idx = (row // 3, col // 3)
                if (
                    board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in boxes[box_idx]
                ):
                    return False

                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[box_idx].add(board[row][col])

        return True
