# n = len(root)
# Time: O(n)
# Space: O(logn)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = self.dfs(root, 0)
        return sum

    def dfs(self, root: Optional[TreeNode], sum: int) -> int:
        if not root:
            return 0
        sum = sum * 10 + root.val
        if not root.left and not root.right:
            return sum
        return self.dfs(root.left, sum) + self.dfs(root.right, sum)
