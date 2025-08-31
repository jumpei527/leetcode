# n = len(instructions)
# Time: O(n)
# Space: O(1)


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = (0, 1)
        cur_pos = (0, 0)

        for instruction in instructions:
            if instruction == "G":
                cur_pos = (
                    cur_pos[0] + direction[0],
                    cur_pos[1] + direction[1]
                )
            if instruction == "L":
                direction = (-direction[1], direction[0])
            elif instruction == "R":
                direction = (direction[1], -direction[0])

        return True if cur_pos == (0, 0) or direction != (0, 1) else False
