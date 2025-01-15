# n = len(obstacleGrid)
# m = len(obstacleGrid[0])
# Time: O(n * m)
# Space: O(1)
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                if i > 0 and j > 0:
                    obstacleGrid[i][j] = (
                        obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                    )
                elif j > 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif i > 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = 1

        return obstacleGrid[-1][-1]
