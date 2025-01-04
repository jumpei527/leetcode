# n: node_count
# Time: O(n)
# Space: O(n)
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = deque()
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)

        prev = root
        while stack:
            curr = stack.pop()
            prev.left = None
            prev.right = curr
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            prev = curr

        return root
