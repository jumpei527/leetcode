# n: node_count
# Time: O(n)
# Space: O(n/2)
from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: 'Node' = None,
        right: 'Node' = None,
        next: 'Node' = None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        stack = deque([root])

        while stack:
            prev = None
            node_count = len(stack)
            for _ in range(node_count):
                curr = stack.popleft()
                if prev:
                    prev.next = curr
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                prev = curr
            prev.next = None

        return root
