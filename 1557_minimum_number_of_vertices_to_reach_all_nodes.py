# n: number of nodes
# m: number of edges
# Time: O(n + m)
# Space: O(n)
from typing import List


class Solution:
    def findSmallestSetOfVertices(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        indegree = [0] * n

        for _, to_node in edges:
            indegree[to_node] += 1

        source_nodes = [idx for idx in range(n) if indegree[idx] == 0]

        return source_nodes
