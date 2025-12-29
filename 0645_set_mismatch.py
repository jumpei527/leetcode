# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_freq = Counter(nums)

        for idx in range(1, len(nums) + 1):
            if num_freq[idx] == 2:
                duplicate = idx
            elif num_freq[idx] == 0:
                missing = idx

        return [duplicate, missing]
