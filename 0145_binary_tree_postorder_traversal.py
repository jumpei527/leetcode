# n: node_count
# Time: O(n)
# Space: O(n)
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        val_list = []
        self.dfs(root, val_list)
        return val_list

    def dfs(
            self, root: Optional[TreeNode], val_list: List[TreeNode]
    ) -> List[int]:
        if not root:
            return

        self.dfs(root.left, val_list)
        self.dfs(root.right, val_list)
        val_list.append(root.val)
