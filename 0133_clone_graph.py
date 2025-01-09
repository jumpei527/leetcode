# n : node_count
# e : edge_count
# Time: O(n+e)
# Space: O(n+e)
from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        stack = deque([node])
        clones = {}
        clones[node.val] = Node(node.val, [])
        while stack:
            curr = stack.popleft()
            curr_clone = clones[curr.val]

            for neig in curr.neighbors:
                if neig.val not in clones:
                    clones[neig.val] = Node(neig.val, [])
                    stack.append(neig)
                curr_clone.neighbors.append(clones[neig.val])

        return clones[node.val]
