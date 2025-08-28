# n = len(nums)
# k = number of unique elements in nums
# Time: O(nlogk)
# Space: O(n)
from collections import defaultdict
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        min_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        most_freq_elements = []
        for _ in range(k):
            _, num = min_heap.pop()
            most_freq_elements.append(num)

        return most_freq_elements
