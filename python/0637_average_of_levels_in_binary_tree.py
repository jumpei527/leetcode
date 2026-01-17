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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return
        ans = []
        queue = deque([root])

        while queue:
            node_count = len(queue)
            average_val = 0
            for _ in range(node_count):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                average_val += cur.val
            ans.append(average_val / node_count)

        return ans
