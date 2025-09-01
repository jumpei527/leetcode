# n = len(moves)
# Time: O(n)
# Space: O(1)


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal_move = 0
        vertical_move = 0

        for direction in moves:
            if direction == "R":
                horizontal_move -= 1
            elif direction == "L":
                horizontal_move += 1
            elif direction == "U":
                vertical_move += 1
            elif direction == "D":
                vertical_move -= 1

        return True if horizontal_move == 0 and vertical_move == 0 else False
