# n = len(preorder)
# Time: O(n^2)
# Space: O(n^2)
from typing import List, Optional, Deque
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        preorder = deque(preorder)

        return self.buildTreeFromDeque(preorder, inorder)

    def buildTreeFromDeque(
        self, preorder: Deque[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        if not inorder:
            return

        idx = inorder.index(preorder.popleft())
        root = TreeNode(inorder[idx])

        root.left = self.buildTreeFromDeque(preorder, inorder[:idx])
        root.right = self.buildTreeFromDeque(preorder, inorder[idx+1:])

        return root
