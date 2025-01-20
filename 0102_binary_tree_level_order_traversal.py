# n: node_count
# Time: O(n)
# Space: O(n)
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        val_list = []

        while queue:
            cur_level = []
            length = len(queue)
            for i in range(length):
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                cur_level.append(cur_node.val)
            val_list.append(cur_level)

        return val_list
