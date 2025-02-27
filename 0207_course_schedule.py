# V = numCourses, E = len(prerequisites)
# Time: O(V + E)
# Space: O(V + E)
from typing import List
from collections import deque


class Solution:
    def canFinish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        graph = [[] for _ in range(numCourses)]
        into_num = [0] * numCourses
        ans = []

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            into_num[course] += 1

        queue = deque()
        for i in range(numCourses):
            if into_num[i] == 0:
                queue.append(i)

        while queue:
            cur = queue.popleft()
            ans.append(cur)

            for next_course in graph[cur]:
                into_num[next_course] -= 1
                if into_num[next_course] == 0:
                    queue.append(next_course)

        return len(ans) == numCourses
