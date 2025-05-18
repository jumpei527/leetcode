# n = len(isConnected)
# Time: O(n^2)
# Space: O(n)
from typing import List


class Solution:
    def findCircleNum(
        self, isConnected: List[List[int]]
    ) -> int:
        provinces_number = 0
        self.visited = set()

        for node in range(len(isConnected)):
            if node not in self.visited:
                provinces_number += 1
                self.visit_connected_node(node, isConnected)

        return provinces_number

    def visit_connected_node(
        self, node: int, isConnected: List[List[int]]
    ) -> None:
        for neighbor in range(len(isConnected)):
            if isConnected[node][neighbor] and neighbor not in self.visited:
                self.visited.add(neighbor)
                self.visit_connected_node(neighbor, isConnected)
