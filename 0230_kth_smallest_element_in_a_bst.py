# n: node_count
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val_list = []
        self.inorder_traversal(root, val_list)
        return val_list[k-1]

    def inorder_traversal(self, root: Optional[TreeNode], val_list):
        if not root:
            return

        self.inorder_traversal(root.left, val_list)
        val_list.append(root.val)
        self.inorder_traversal(root.right, val_list)
