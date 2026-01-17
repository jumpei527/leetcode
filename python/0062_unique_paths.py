# Time: O(mn)
# Space: O(mn)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_num = [[0] * n for _ in range(m)]

        for row in range(0, m):
            path_num[row][0] = 1
        for col in range(0, n):
            path_num[0][col] = 1

        for row in range(1, m):
            for col in range(1, n):
                path_num[row][col] = (
                    path_num[row-1][col] + path_num[row][col-1]
                )

        return path_num[-1][-1]
