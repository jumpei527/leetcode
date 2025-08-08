# n = len(nums)
# Time: O(n)
# Space: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        freq = defaultdict(int)

        for num in nums:
            count += freq[num - k]
            count += freq[num + k]

            freq[num] += 1

        return count
