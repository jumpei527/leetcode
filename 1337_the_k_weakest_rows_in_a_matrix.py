# n = len(mat)
# m = len(mat[i])
# Time: O(nlogm + nlogn)
# Space: O(n)
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count_1 = []
        for i in range(len(mat)):
            left = -1
            right = len(mat[0])
            while right - left > 1:
                mid = (left + right) // 2
                if mat[i][mid] == 1:
                    left = mid
                else:
                    right = mid
            count_1.append([right, i])
        count_1.sort()
        return [count[1] for count in count_1[:k]]
