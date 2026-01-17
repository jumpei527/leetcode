# n: number of nodes
# Time: O(n)
# Space: O(n)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Count the number of "good" nodes in a binary tree.
        A node is considered "good" if it is greater than or equal to all
        nodes on the path from the root to that node.

        Args:
            root (TreeNode): The root of the binary tree.

        Returns:
            int: The number of "good" nodes in the binary tree.

        Example:
            >>> root = TreeNode(3, TreeNode(1), TreeNode(4))
            >>> Solution().goodNodes(root)
            2
        """

        def dfs_count_good_nodes(node: TreeNode, max_val: int) -> int:
            """
            Perform a preorder traversal of the tree, counting "good" nodes.

            Args:
                node (TreeNode): The current node in the traversal.
                max_val (int): The maximum value seen on the path from the root
                               to the current node.

            Returns:
                int: The count of "good" nodes in the subtree rooted at `node`.

            Example:
                >>> root = TreeNode(3, TreeNode(1), TreeNode(4))
                >>> dfs_count_good_nodes(root, float('-inf'))
                2
            """
            if not node:
                return 0

            is_good = node.val >= max_val
            max_val = max(max_val, node.val)

            left_count = dfs_count_good_nodes(node.left, max_val)
            right_count = dfs_count_good_nodes(node.right, max_val)

            return is_good + left_count + right_count

        return dfs_count_good_nodes(root, root.val)
