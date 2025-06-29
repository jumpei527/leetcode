# n: number of nodes
# Time: O(n)
# Space: O(1)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:
        if not root:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val == key:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            min_node = self.find_min_node(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, root.val)

        return root

    def find_min_node(self, root: Optional[TreeNode]) -> int:
        min_node = root

        while min_node.left:
            min_node = min_node.left

        return min_node
