# n = len(target)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        cur_idx = 0
        target_len = len(target)
        for num in range(1, n + 1):
            if cur_idx == target_len:
                return operations
            operations.append("Push")
            if target[cur_idx] != num:
                operations.append("Pop")
            else:
                cur_idx += 1

        return operations
