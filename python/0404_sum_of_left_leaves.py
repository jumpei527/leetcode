# Time: O(n)
# Space: O(n)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        sum_leaves = 0
        if root.left and not root.left.left and not root.left.right:
            sum_leaves += root.left.val
        if root.left:
            sum_leaves += self.sumOfLeftLeaves(root.left)
        if root.right:
            sum_leaves += self.sumOfLeftLeaves(root.right)
        return sum_leaves
