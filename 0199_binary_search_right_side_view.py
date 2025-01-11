# n: node_count
# Time: O(n)
# Space: O(n/2)
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack = deque([root])

        while stack:
            depth = len(stack)
            for i in range(depth):
                cur = stack.popleft()
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
                if i == depth - 1:
                    ans.append(cur.val)

        return ans
