# n = len(citations)
# Time: O(nlogn)
# Space: O(1)
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0

        for i in range(len(citations)):
            if h_index + 1 > citations[i]:
                return h_index
            h_index += 1

        return h_index
