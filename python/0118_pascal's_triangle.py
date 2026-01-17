from typing import List


class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prevRow = self.generate(numRows - 1)
        newRow = [1] * numRows

        for i in range(1, numRows-1):
            newRow[i] = prevRow[-1][i-1] + prevRow[-1][i]

        prevRow.append(newRow)
        return prevRow


class Solution2:
    # Time: O(n^2)
    # Space: O(n^2)
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            newRow = [1] * (i+1)
            for j in range(1, i):
                newRow[j] = ans[-1][j-1] + ans[-1][j]
            ans.append(newRow)
        return ans
