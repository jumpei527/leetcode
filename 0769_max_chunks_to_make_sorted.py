# n = len(arr)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_num = 0
        chunk_count = 0

        for i, num in enumerate(arr):
            max_num = max(num, max_num)
            if max_num == i:
                chunk_count += 1

        return chunk_count
