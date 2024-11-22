# n = len(stones)
# Time: O(nlogn)
# Space: O(1)
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [n * (-1) for n in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first_stone = heapq.heappop(stones)
            second_stone = heapq.heappop(stones)
            if first_stone != second_stone:
                heapq.heappush(stones, first_stone - second_stone)
        if not stones:
            return 0
        return stones[0] * (-1)
