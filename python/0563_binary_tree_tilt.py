# n: number of nodes
# Time: O(n)
# Space: O(logn)
from typing import Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        """
        Receive the root of a binary tree and return the sum of the tilts
        of all its nodes.
        The tilt of a node is the absolute difference between the sum of
        all node values in its left subtree and the sum of all node values
        in its right subtree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The sum of the tilts of all nodes in the binary tree.

        Examples:
            >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
            >>> Solution().findTilt(root)
            1
        """
        self.tilt_sum = 0
        self.computeSubtreeSum(root)
        return self.tilt_sum

    def computeSubtreeSum(self, root: Optional[TreeNode]) -> int:
        """
        Compute the sum of all node values in the subtree rooted at the
        given node while updating the tilt sum of the binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the subtree.

        Returns:
            int: The sum of all node values in the subtree rooted at the
            given node.

        Examples:
            >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
            >>> Solution().computeSubtreeSum(root)
            6
        """
        if not root:
            return 0

        left_sum = self.computeSubtreeSum(root.left)
        right_sum = self.computeSubtreeSum(root.right)
        self.tilt_sum += abs(left_sum - right_sum)

        return left_sum + right_sum + root.val


class TestFindTilt(unittest.TestCase):
    def build_tree(self, values, index=0):
        """build a binary tree from a list representation"""
        if index >= len(values) or values[index] is None:
            return None

        root = TreeNode(values[index])
        root.left = self.build_tree(values, 2 * index + 1)
        root.right = self.build_tree(values, 2 * index + 2)
        return root

    def test_balanced_tree(self):
        """Test with a balanced binary tree"""
        root = self.build_tree([21, 7, 14, 1, 1, 2, 2, 3, 3])
        self.assertEqual(Solution().findTilt(root), 9)

    def test_tree_with_null(self):
        """Test with a binary tree containing None values"""
        root = self.build_tree([4, 2, 9, 3, 5, None, 7])
        self.assertEqual(Solution().findTilt(root), 15)

    def test_empty_tree(self):
        """Test with an empty tree"""
        self.assertEqual(Solution().findTilt(None), 0)


if __name__ == "__main__":
    unittest.main()
