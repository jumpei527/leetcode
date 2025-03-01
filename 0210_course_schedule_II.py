# V = numCourses, E = len(prerequisites)
# Time: O(V + E)
# Space: O(V + E)
from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        into_num = [0] * numCourses
        course_order = []

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            into_num[course] += 1

        queue = deque()

        for i in range(numCourses):
            if into_num[i] == 0:
                queue.append((i, graph[i]))

        while queue:
            course, prerequisites = queue.popleft()
            course_order.append(course)
            for prerequisite in prerequisites:
                into_num[prerequisite] -= 1
                if into_num[prerequisite] == 0:
                    queue.append((prerequisite, graph[prerequisite]))

        if len(course_order) != numCourses:
            return []

        return course_order
