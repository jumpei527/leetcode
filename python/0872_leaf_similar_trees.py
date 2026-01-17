# n: the number of nodes in root1
# m: the number of nodes in root2
# Time: O(n + m)
# Space: O(n + m)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        root1_leaf_value = []
        root2_leaf_value = []

        self.collect_leaf_value(root1, root1_leaf_value)
        self.collect_leaf_value(root2, root2_leaf_value)

        return root1_leaf_value == root2_leaf_value

    def collect_leaf_value(
        self, root: Optional[TreeNode], leaf_value: Optional[TreeNode]
    ) -> None:
        if not root:
            return

        if not root.left and not root.right:
            leaf_value.append(root.val)
            return

        self.collect_leaf_value(root.left, leaf_value)
        self.collect_leaf_value(root.right, leaf_value)
