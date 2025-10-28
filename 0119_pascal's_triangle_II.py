# n = rowIndex
# Time: O(n^2)
# Space: O(n)
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal_row = [0] * (rowIndex + 1)
        pascal_row[0] = 1

        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                pascal_row[j] += pascal_row[j - 1]

        return pascal_row
