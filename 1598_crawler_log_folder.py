# n = len(logs)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dir_list = []

        for operation in logs:
            directory = operation.rstrip("/")
            if directory == "..":
                if dir_list:
                    dir_list.pop()
            elif directory == ".":
                continue
            else:
                dir_list.append(directory)

        return len(dir_list)
