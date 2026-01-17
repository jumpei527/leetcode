# n = len(nums)
# Time: O(n)
# Space: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        pairs_count = 0
        for freq in freq_map.values():
            if freq > 1:
                pairs_count += freq * (freq - 1) // 2

        return pairs_count
