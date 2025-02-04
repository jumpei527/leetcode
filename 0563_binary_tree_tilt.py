# n: number of nodes
# Time: O(n)
# Space: O(logn)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sum_tilt = 0

        def computeSubtreeTilt(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left_sum = computeSubtreeTilt(root.left)
            right_sum = computeSubtreeTilt(root.right)
            self.sum_tilt += abs(left_sum - right_sum)

            return left_sum + right_sum + root.val

        computeSubtreeTilt(root)
        return self.sum_tilt
