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


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.cur_index = 0
        self.inorder_traversal(root)

    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        self.arr.append(root.val)
        self.inorder_traversal(root.right)

    def next(self) -> int:
        val = self.arr[self.cur_index]
        self.cur_index += 1
        return val

    def hasNext(self) -> bool:
        return self.cur_index <= len(self.arr) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
