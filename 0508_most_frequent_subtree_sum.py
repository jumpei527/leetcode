# n is the number of nodes
# Time: O(n)
# Space: O(n)
from collections import Counter
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.counter = Counter()

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.compute_subtree_sum(root)

        max_freq = max(self.counter.values())
        max_freq_values = []
        for total, freq in self.counter.items():
            if freq == max_freq:
                max_freq_values.append(total)

        return max_freq_values

    def compute_subtree_sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_sum = self.compute_subtree_sum(root.left)
        right_sum = self.compute_subtree_sum(root.right)
        total = root.val + left_sum + right_sum

        self.counter[total] += 1

        return total
