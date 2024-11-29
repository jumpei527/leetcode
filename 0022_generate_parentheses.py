# Time: O(2**n)
# Space: O(2**n)
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                ans.append(s)
                return
            if left < n:
                dfs(left+1, right, s + "(")
            if left > right:
                dfs(left, right+1, s + ")")

        ans = []
        dfs(0, 0, "")
        return ans
