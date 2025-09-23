# n = len(time)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_freq = {}

        pairs_cnt = 0
        for sec in time:
            remainder = sec % 60
            if remainder == 0:
                pairs_cnt += remainder_freq.get(0, 0)
            else:
                pairs_cnt += remainder_freq.get(60 - remainder, 0)
            remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1

        return pairs_cnt
