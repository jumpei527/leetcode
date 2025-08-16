# n = len(rowCosts)
# m = len(colCosts)
# Time: O(n + m)
# Space: O(1)
from typing import List


class Solution:
    def minCost(
        self,
        startPos: List[int],
        homePos: List[int],
        rowCosts: List[int],
        colCosts: List[int]
    ) -> int:
        total_cost = 0

        if startPos[0] < homePos[0]:
            for row_idx in range(startPos[0], homePos[0]):
                total_cost += rowCosts[row_idx+1]
        else:
            for row_idx in range(homePos[0], startPos[0]):
                total_cost += rowCosts[row_idx]

        if startPos[1] < homePos[1]:
            for col_idx in range(startPos[1], homePos[1]):
                total_cost += colCosts[col_idx+1]
        else:
            for col_idx in range(homePos[1], startPos[1]):
                total_cost += colCosts[col_idx]

        return total_cost
