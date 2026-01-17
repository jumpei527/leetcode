# n = len(root)
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        inorder_list = []
        self.makeInorderList(root, inorder_list)
        for i in range(1, len(inorder_list)):
            if inorder_list[i] <= inorder_list[i-1]:
                return False
        return True

    def makeInorderList(self, root, inorder_list):
        if not root:
            return
        self.makeInorderList(root.left, inorder_list)
        inorder_list.append(root.val)
        self.makeInorderList(root.right, inorder_list)
        return
