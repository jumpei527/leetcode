# n = len(equations)
# m = len(queries)
# Time: O(nm)
# Space: O(n + m)
from typing import List
from collections import defaultdict, deque


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:
        self.graph = defaultdict(dict)

        for idx, equation in enumerate(equations):
            start, end = equation
            self.graph[start][end] = values[idx]
            self.graph[end][start] = 1 / values[idx]

        ans = []
        for start, end in queries:
            ans.append(self.bfs(start, end))
        return ans

    def bfs(
        self, start: str, end: str
    ) -> float:
        if start not in self.graph or end not in self.graph:
            return -1.0
        if start == end:
            return 1.0
        visited = set()
        queue = deque()
        queue.append([start, 1.0])

        while queue:
            cur, num = queue.popleft()
            if cur == end:
                return num

            visited.add(cur)
            for _next, next_num in self.graph[cur].items():
                if _next in visited:
                    continue
                queue.append([_next, next_num * num])

        return -1.0
