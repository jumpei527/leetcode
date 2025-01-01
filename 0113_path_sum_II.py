# n = len(root)
# Time: O(nlogn)
# Space: O(nlogn)
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(
            self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        if not root:
            return []
        ans = []
        stack = [(root, targetSum - root.val, [root.val])]

        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                ans.append(ls)
            if curr.left:
                stack.append(
                    (curr.left, val - curr.left.val, ls + [curr.left.val])
                )
            if curr.right:
                stack.append(
                    (curr.right, val - curr.right.val, ls + [curr.right.val])
                )
        return ans
