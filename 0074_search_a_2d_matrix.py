# n = len(matrix), m = len(matrix[0])
# Time: O(log(n) + log(m))
# Space: O(1)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = -1
        bottom = len(matrix)
        while bottom - top > 1:
            mid = (top + bottom) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                bottom = mid
            else:
                top = mid

        left = -1
        right = len(matrix[0])
        while right - left > 1:
            mid = (left + right) // 2
            if matrix[top][mid] == target:
                return True
            elif matrix[top][mid] > target:
                right = mid
            else:
                left = mid

        return False
