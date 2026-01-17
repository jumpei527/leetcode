# n: node_count
# Time: O(n)
# Space: O(n)
from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        zigzag_val = []
        is_even = False

        while queue:
            n = len(queue)
            cur_level = []
            for _ in range(n):
                cur_node = queue.popleft()
                cur_level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            if is_even:
                zigzag_val.append(cur_level[::-1])
            else:
                zigzag_val.append(cur_level)
            is_even = not is_even
        return zigzag_val
