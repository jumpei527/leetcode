# n = len(root)
# Time: O(nlogn)
# Space: O(n)
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        val_list = self.inorder_traversal(root)
        sorted_list = sorted([node.val for node in val_list])
        for i in range(len(val_list)):
            val_list[i].val = sorted_list[i]
        return root

    
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[TreeNode]:
        val_list = []
        self.dfs(root, val_list)
        return val_list
    
    def dfs(self, root: Optional[TreeNode], val_list: List[TreeNode]) -> List[TreeNode]:
        if not root:
            return
        self.dfs(root.left, val_list)
        val_list.append(root)
        self.dfs(root.right, val_list)

