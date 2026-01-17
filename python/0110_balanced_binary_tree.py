# n = len(root)
# Time: O(n)
# Space: O(n)
from typing import Optional, NamedTuple, List
from collections import deque
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeStatus(NamedTuple):
    isBalanced: bool
    height: int


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is height-balanced.
        A binary tree is balanced if the depth of the two subtrees of
        every node never differs by more than 1.

        Args:
            root (Optional[TreeNode]): Root node of the binary tree.

        Returns:
            bool: True if the tree is balanced, False otherwise.

        Examples:
            >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
            >>> Solution().isBalanced(root)
            True
        """
        return self.computeBalancedHeight(root).isBalanced

    def computeBalancedHeight(self, root: Optional[TreeNode]) -> TreeStatus:
        """
        Recursively calculates the height of the tree while checking for
        balance.

        Args:
            root (TreeNode): Current node being evaluated.

        Returns:
            TreeStatus: A NamedTuple containing:
                - isBalanced (bool): True if the subtree is balanced,
                  False otherwise.
                - height (int): Height of the subtree if balanced.
                  If unbalanced, the height is -1.

        Examples:
            >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
            >>> Solution().computeBalancedHeight(root)
            TreeStatus(isBalanced=True, height=2)
        """
        if not root:
            return TreeStatus(True, 0)

        left_status = self.computeBalancedHeight(root.left)
        right_status = self.computeBalancedHeight(root.right)

        if not left_status.isBalanced or not right_status.isBalanced:
            return TreeStatus(False, -1)

        if abs(left_status.height - right_status.height) > 1:
            return TreeStatus(False, -1)

        return TreeStatus(
            True, max(left_status.height, right_status.height) + 1
        )


class TestIsBalanced(unittest.TestCase):
    def arrayToTree(self, nums: List[Optional[int]]) -> Optional[TreeNode]:
        """
        Converts a list of values into a binary tree.
        """
        if not nums:
            return None

        root = TreeNode(nums[0])
        queue = deque([root])
        i = 1

        while i < len(nums):
            node = queue.popleft()

            if i < len(nums) and nums[i] is not None:
                node.left = TreeNode(nums[i])
                queue.append(node.left)
            i += 1

            if i < len(nums) and nums[i] is not None:
                node.right = TreeNode(nums[i])
                queue.append(node.right)
            i += 1

        return root

    def test_isBalanced_balanced_tree(self):
        root = self.arrayToTree([1, 2, 3, 4, 5, 6, 7])
        expected = True
        result = Solution().isBalanced(root)
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )

    def test_isBalanced_unbalanced_tree(self):
        root = self.arrayToTree([1, 2, 5, 3, None, None, None, 4])
        expected = False
        result = Solution().isBalanced(root)
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )

    def test_isBalanced_empty_tree(self):
        root = self.arrayToTree([])
        expected = True
        result = Solution().isBalanced(root)
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )
