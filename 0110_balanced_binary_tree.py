# n = len(root)
# Time: O(n)
# Space: O(n)
from typing import Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
        if not root:
            return True

        return self.computeBalancedHeight(root) >= 0

    def computeBalancedHeight(self, root) -> int:
        """
        Recursively calculates the height of the tree while checking for
        balance.
        If an imbalance is found, the function returns -1.

        Args:
            root (TreeNode): Current node being evaluated.

        Returns:
            int: Height of the subtree if balanced, -1 if unbalanced.

        Examples:
            >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
            >>> Solution().computeBalancedHeight(root)
            2
        """
        if not root:
            return 0

        left_height = self.computeBalancedHeight(root.left)
        right_height = self.computeBalancedHeight(root.right)

        if left_height == -1 or right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1


class TestIsBalanced(unittest.TestCase):
    def test_isBalanced_balanced_tree(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7))
        )
        expected = True
        result = Solution().isBalanced(root)
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )

    def test_isBalanced_unbalanced_tree(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(4), None), None),
            TreeNode(5)
        )
        expected = False
        result = Solution().isBalanced(root)
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )

    def test_isBalanced_empty_tree(self):
        root = None
        expected = True
        result = Solution().isBalanced(root)
        self.assertEqual(
            result, expected, f"Expected {expected} but got {result}"
        )
