# Time: O(kn^2)
# Space: O(n^2)


class Solution:
    def knightProbability(
        self, n: int, k: int, row: int, column: int
    ) -> float:
        current_board = [[0] * n for _ in range(n)]
        current_board[row][column] = 1

        KNIGHT_MOVES = [
            (2, 1),
            (1, 2),
            (-2, 1),
            (-1, 2),
            (2, -1),
            (1, -2),
            (-2, -1),
            (-1, -2),
        ]

        for _ in range(k):
            next_board = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if current_board[r][c] > 0:
                        for dr, dc in KNIGHT_MOVES:
                            next_r = r + dr
                            next_c = c + dc
                            if 0 <= next_r < n and 0 <= next_c < n:
                                next_board[next_r][next_c] += (
                                    current_board[r][c] / 8
                                )
            current_board = next_board

        probability = 0
        for r in range(n):
            for c in range(n):
                probability += current_board[r][c]

        return probability
