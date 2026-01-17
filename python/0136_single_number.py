# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
